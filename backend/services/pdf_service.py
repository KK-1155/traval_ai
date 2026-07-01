from fpdf import FPDF


def create_pdf(
    destination,
    weather,
    itinerary
):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font(
        "Arial",
        size=12
    )

    pdf.cell(
        0,
        10,
        "Myanmar AI Travel Planner",
        ln=True
    )

    pdf.cell(
        0,
        10,
        f"Destination: {destination}",
        ln=True
    )

    pdf.cell(
        0,
        10,
        f"Weather: {weather}",
        ln=True
    )

    pdf.multi_cell(
        0,
        10,
        itinerary
    )

    filename = (
        f"{destination}_plan.pdf"
    )

    pdf.output(
        filename
    )

    return filename