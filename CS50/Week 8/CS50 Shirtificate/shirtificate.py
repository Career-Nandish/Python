from fpdf import FPDF

class Shirtificate(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 40)
        self.cell(0, 55, "CS50 Shirtificate", align="C")

    def create_shirtificate(self, name):
        self.add_page()
        self.set_auto_page_break(auto=True, margin=15)
        self.set_margins(left=15, top=15, right=15)

        self.set_font("Helvetica", size=40)
        self.set_text_color(255, 255, 255)

        self.cell(5, 10, name, align="C")

        self.image("onlyface.png", x=68, y=0, w=100, h=100)
        self.image("shirtificate.png", x=15, y=78, w=190, h=190)

        self.text(65, 140, name)

def main():
    name = input("Name: ")
    shirtificate = Shirtificate(orientation="P", unit="mm", format="A4")
    shirtificate.create_shirtificate(f"Harvard's CS50")
    shirtificate.output("shirtificate.pdf")

if __name__ == "__main__":
    main()