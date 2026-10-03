"""Build toshakhana_report.pdf from data/toshakhana_clean.csv.

Run the notebook first (it writes the clean CSV), then: python make_report.py
"""
import io

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (Image, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle)

M = 1e6
ACCENT = colors.HexColor("#1F4E79")
df = pd.read_csv("data/toshakhana_clean.csv", parse_dates=["Date"])
df["Paid0"] = df["Paid"].fillna(0)
retained = df["Status"].eq("Retained")
free = retained & df["Paid0"].eq(0)

ss = getSampleStyleSheet()
H1 = ParagraphStyle("H1", parent=ss["Title"], textColor=ACCENT, fontSize=22, spaceAfter=4)
H2 = ParagraphStyle("H2", parent=ss["Heading2"], textColor=ACCENT, spaceBefore=10, spaceAfter=6)
P = ParagraphStyle("P", parent=ss["BodyText"], fontSize=9.5, leading=13)
SMALL = ParagraphStyle("S", parent=P, fontSize=8, leading=10, textColor=colors.HexColor("#555555"))
CELL = ParagraphStyle("C", parent=P, fontSize=8, leading=10)


def money(v):
    return "–" if pd.isna(v) else f"{v:,.0f}"


def mil(v):
    return f"{v / M:,.1f}"


def table(rows, widths=None, align_right_from=1):
    rows = [[Paragraph(str(c), CELL) if isinstance(c, str) and len(c) > 28 else c for c in r] for r in rows]
    t = Table(rows, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), ACCENT), ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"), ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("ALIGN", (align_right_from, 0), (-1, -1), "RIGHT"), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F2F5F9")]),
        ("LINEBELOW", (0, 0), (-1, -1), 0.25, colors.HexColor("#CCCCCC")),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return t


def fig_image(fig, width=17 * cm):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=170, bbox_inches="tight")
    plt.close(fig)
    buf.seek(0)
    w, h = fig.get_size_inches()
    return Image(buf, width=width, height=width * h / w)


def group_table(col, top=None, min_label=None):
    g = df.groupby(col).agg(n=("Gift", "size"), a=("Assessed", "sum"), p=("Paid", "sum"),
                            med=("Assessed", "median")).sort_values("a", ascending=False)
    if top:
        g = g.head(top)
    rows = [[min_label or col, "Records", "Assessed (PKR m)", "Paid (PKR m)", "Paid %", "Median (PKR)"]]
    for k, r in g.iterrows():
        rows.append([k, f"{r.n:,.0f}", mil(r.a), mil(r.p), f"{r.p / r.a * 100:.1f}" if r.a else "–", money(r.med)])
    return g, table(rows, [5 * cm, 2 * cm, 3 * cm, 2.6 * cm, 1.8 * cm, 2.6 * cm])


plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False, "font.size": 9})
story = []

# ---------- page 1: headline ----------
story += [Paragraph("Pakistan Toshakhana Files", H1),
          Paragraph("Statistical summary of official gift records, 2002–2022", ss["Heading3"]),
          Paragraph("Source: Kaggle dataset <i>zusmani/pakistan-toshakhana-files</i> (refined CSV). "
                    "All amounts are nominal Pakistani rupees and are not inflation-adjusted. "
                    "Figures are computed from the dataset as published and inherit its extraction errors and gaps.", SMALL),
          Spacer(1, 8), Paragraph("Headline numbers", H2)]
tot_a, tot_p = df["Assessed"].sum(), df["Paid"].sum()
s = df["Assessed"].fillna(0).sort_values(ascending=False)
story.append(table([
    ["Metric", "Value"],
    ["Gift records", f"{len(df):,}"],
    ["Period covered", f"{df['Date'].min():%d %b %Y} – {df['Date'].max():%d %b %Y}"],
    ["Total assessed value", f"PKR {mil(tot_a)} million"],
    ["Total paid by recipients to retain gifts", f"PKR {mil(tot_p)} million ({tot_p / tot_a * 100:.1f}% of assessed)"],
    ["Records retained by the recipient", f"{retained.sum():,} ({retained.mean() * 100:.1f}%)"],
    ["Retained at zero cost", f"{free.sum():,} ({free.sum() / retained.sum() * 100:.1f}% of retained), "
                              f"worth PKR {mil(df.loc[free, 'Assessed'].sum())} million"],
    ["Median / mean assessed value", f"PKR {money(df['Assessed'].median())} / PKR {money(df['Assessed'].mean())}"],
    ["Gifts assessed at PKR 1 million or more", f"{(df['Assessed'] >= M).sum()}"],
    ["Share of value in the top 10 / top 100 gifts", f"{s.head(10).sum() / tot_a * 100:.0f}% / {s.head(100).sum() / tot_a * 100:.0f}%"],
], [8 * cm, 9 * cm], align_right_from=2))

yr = df.groupby("Year").agg(n=("Gift", "size"), a=("Assessed", "sum"), p=("Paid", "sum"))
yr.index = yr.index.astype(int)
fig, ax = plt.subplots(1, 2, figsize=(11, 3.4))
ax[0].bar(yr.index, yr["n"], color="#1F4E79"); ax[0].set_title("Gift records per year")
ax[1].bar(yr.index - 0.2, yr["a"] / M, 0.4, label="Assessed", color="#C44E52")
ax[1].bar(yr.index + 0.2, yr["p"] / M, 0.4, label="Paid", color="#55A868")
ax[1].set_title("Assessed value vs amount paid (PKR million)"); ax[1].legend(frameon=False)
story += [Paragraph("Over time", H2), fig_image(fig)]
hi, lo = yr["a"].idxmax(), yr["a"].idxmin()
story.append(Paragraph(
    f"Highest-value year: <b>{hi}</b> (PKR {mil(yr.loc[hi, 'a'])} m from {yr.loc[hi, 'n']} records). "
    f"Lowest-value year: <b>{lo}</b> (PKR {mil(yr.loc[lo, 'a'])} m from {yr.loc[lo, 'n']} records). "
    f"Most records: <b>{yr['n'].idxmax()}</b> ({yr['n'].max()}); fewest: <b>{yr['n'].idxmin()}</b> ({yr['n'].min()}).", P))
story.append(PageBreak())

# ---------- page 2: who ----------
story.append(Paragraph("By affiliation", H2))
story.append(Paragraph("Affiliation is the dataset author's label; about a quarter of rows have none, "
                       "so these totals are indicative only.", SMALL))
aff, t = group_table("Affiliation")
story.append(t)

story.append(Paragraph("By office holder (household)", H2))
story.append(Paragraph("Recipient names were matched to 19 prominent office holders. Gifts recorded against "
                       "spouses and children are counted under the office holder.", SMALL))
sub = df[df["Person"] != "Other"]
g = sub.groupby("Person").agg(n=("Gift", "size"), a=("Assessed", "sum"), p=("Paid", "sum"),
                              mx=("Assessed", "max")).sort_values("a", ascending=False)
fam = df[df["Family"]].groupby("Person")["Assessed"].sum().reindex(g.index).fillna(0)
rows = [["Person", "Records", "Assessed (PKR m)", "of which family", "Paid (PKR m)", "Paid %", "Largest gift (PKR m)"]]
for k, r in g.iterrows():
    rows.append([k, f"{r.n:,.0f}", mil(r.a), mil(fam[k]), mil(r.p), f"{r.p / r.a * 100:.1f}", mil(r.mx)])
story.append(table(rows, [4.4 * cm, 1.7 * cm, 2.7 * cm, 2.4 * cm, 2.2 * cm, 1.4 * cm, 2.6 * cm]))
story.append(PageBreak())

# ---------- page 3: what ----------
story.append(Paragraph("By item category", H2))
story.append(Paragraph("The source leaves the category blank for 44.5% of rows; blanks were filled with keyword rules.", SMALL))
cat, t = group_table("Category")
story.append(t)
fig, ax = plt.subplots(1, 2, figsize=(11, 3.6))
cat["n"].sort_values().plot.barh(ax=ax[0], color="#1F4E79", title="Records by category"); ax[0].set_ylabel("")
(cat["a"] / M).sort_values().plot.barh(ax=ax[1], color="#C44E52", title="Assessed value by category (PKR million)")
ax[1].set_ylabel("")
fig.tight_layout()
story += [Spacer(1, 6), fig_image(fig)]

story.append(Paragraph("What happened to the gifts", H2))
st = df.groupby("Status").agg(n=("Gift", "size"), a=("Assessed", "sum")).sort_values("n", ascending=False)
rows = [["Status", "Records", "% of records", "Assessed (PKR m)"]]
for k, r in st.iterrows():
    rows.append([k, f"{r.n:,.0f}", f"{r.n / len(df) * 100:.1f}", mil(r.a)])
story.append(table(rows, [7 * cm, 3 * cm, 3 * cm, 4 * cm]))
story.append(PageBreak())

# ---------- page 4: records ----------
def gift_rows(d, n):
    rows = [["Date", "Gift", "Recipient", "Assessed", "Paid", "Status"]]
    for _, r in d.head(n).iterrows():
        gift = r["Gift"] if len(r["Gift"]) < 95 else r["Gift"][:92] + "…"
        rows.append([f"{r['Date']:%d %b %Y}" if pd.notna(r["Date"]) else "–", Paragraph(gift, CELL),
                     Paragraph(r["Recipient"], CELL), money(r["Assessed"]), money(r["Paid"]),
                     Paragraph(r["Status"], CELL)])
    return table(rows, [1.9 * cm, 5.6 * cm, 4.2 * cm, 2.1 * cm, 1.9 * cm, 2.3 * cm], align_right_from=3)


story += [Paragraph("15 most valuable gifts", H2), gift_rows(df.nlargest(15, "Assessed"), 15),
          Paragraph("Most valuable gifts retained at zero cost", H2),
          gift_rows(df[free].nlargest(8, "Assessed"), 8),
          Paragraph("Lowest assessed gifts (non-zero)", H2),
          gift_rows(df[df["Assessed"] > 0].nsmallest(6, "Assessed"), 6)]

story.append(Paragraph("Data-quality notes", H2))
story.append(Paragraph(
    f"{(df['Assessed'] == 0).sum()} records carry an assessed value of zero; "
    f"{(df['Paid'] > df['Assessed']).sum()} records show a payment larger than the assessed value, which points to "
    f"extraction errors in the source; {(df['Affiliation'] == 'Unlabelled').sum()} records have no affiliation; "
    f"{(df['Person'] == 'Other').sum()} records are not matched to one of the 19 named office holders. "
    "16 exact duplicate rows were removed.", P))


def footer(canvas, doc):
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(colors.grey)
    canvas.drawString(2 * cm, 1.1 * cm, "Pakistan Toshakhana Files — statistical summary")
    canvas.drawRightString(A4[0] - 2 * cm, 1.1 * cm, f"Page {doc.page}")


SimpleDocTemplate("toshakhana_report.pdf", pagesize=A4, leftMargin=2 * cm, rightMargin=2 * cm,
                  topMargin=1.6 * cm, bottomMargin=1.8 * cm,
                  title="Pakistan Toshakhana Files — statistical summary").build(
    story, onFirstPage=footer, onLaterPages=footer)
print("wrote toshakhana_report.pdf")
