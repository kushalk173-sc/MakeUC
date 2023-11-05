import flet as ft
import cv2

def main(page: ft.Page):

    page.title = "Basic elevated buttons"
    t = ft.Tabs(

        selected_index=1,
        animation_duration=300,


        tabs = [

            ft.Tab(
                text="Trash Detector", icon="camera_alt_outlined",
                
                content=ft.ElevatedButton(
                    width=50,
                    content=ft.Container(
                        content=ft.Column(
                            [
                                
                                ft.Text(value="Compound button", size=20),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=5,
                        ),
                        padding=ft.padding.all(10),
                    ),
                ),
            ),

            ft.Tab(
                text="Trash Info", icon="info_outlined",
                
                content=
                    ft.Text("Recycling: Recycling is the process of converting waste materials into reusable objects, reducing the consumption of new raw materials. It plays a crucial role in conserving resources and minimizing environmental impact. Here are some examples of items that can typically be recycled:\n"+

                            "Paper: Newspapers, magazines, cardboard, office paper.\n"+
                            "Plastics: Bottles (with certain exceptions, see below), containers, packaging materials (check for recycling symbols).\n"+
                            "Glass: Bottles, jars.\n"+
                            "Metals: Aluminum cans, steel cans.\n"+
                            "Types of Plastics that Can Be Recycled:\n"+
                            "PETE (Polyethylene Terephthalate): Clear plastic bottles, food containers.\n"+
                            "HDPE (High-Density Polyethylene): Milk jugs, detergent bottles, plastic bags.\n"+
                            "PVC (Polyvinyl Chloride): Pipes, vinyl flooring, some plastic containers.\n"+
                            "LDPE (Low-Density Polyethylene): Plastic bags, shrink wrap, garment bags.\n"+
                            "PP (Polypropylene): Yogurt cups, syrup bottles, caps, straws.\n"+
                            "PS (Polystyrene): Styrofoam, disposable coffee cups, plastic cutlery.\n"+
                            "Other Plastics: Some plastics fall into this category and should be checked for specific recycling guidelines.\n"+
                            "Plastics that Cannot Be Recycled:\n"+
                            
                            "\nPlastic Bags: These can get tangled in recycling machinery.\n"+
                            "Styrofoam: Commonly used in packaging, not widely recyclable.\n"+
                            "Plastic Straws: Too small to be sorted properly.\n"+
                            "Plastic Utensils: Forks, spoons, knives, and other single-use utensils.\n"+

                            "\nLandfill:\n"+
                            "Landfills are sites designated for the disposal of waste materials by burial. Items that end up in landfills are not biodegradable and can take hundreds or even thousands of years to decompose. Common landfill items include:\n"+
                            "Non-Recyclable Plastics: Plastic items that cannot be recycled.\n"+
                            "Certain Electronics: Old computers, batteries, and electronic devices.\n"+
                            "Non-Recyclable Glass: Certain types of glass not suitable for recycling.\n"+
                            "Broken or Unusable Items: Items that cannot be repaired or repurposed.\n"+
                            "Some Textiles: Fabrics that do not decompose easily.\n"+

                            "\nCompost:\n"+
                            "Composting is the natural process of recycling organic material into a rich soil conditioner. Composting is an eco-friendly way to dispose of organic waste. Here are examples of compostable items:\n"+
                            "Fruit and Vegetable Scraps: Peels, cores, and leftovers.\n"+
                            "Coffee Grounds and Filters: Used coffee grounds and paper filters.\n"+
                            "Eggshells: Crushed eggshells provide beneficial calcium to the compost.\n"+
                            "Grass Clippings and Leaves: Lawn trimmings and leaves from trees and plants.\n"+
                            "Paper Products: Newspaper, shredded paper, and cardboard (without glossy coatings).\n"+
                            "Plant Trimmings: Pruned branches, flowers, and other plant materials.\n"+
                            "By providing clear information on recycling, landfill, and compost, along with specific examples, your users will have a better understanding of proper waste disposal practices, encouraging a more environmentally conscious approach to handling their waste.\n"),
                    ),
        ],
        expand = 1,
    )

    page.add(t)
def open_camera_and_capture_photo(camera_index=0, output_file="captured_photo.jpg"):

    cap = cv2.VideoCapture(0)
    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open the camera.")
    else:
        while True:
            # Capture a frame from the camera
            ret, frame = cap.read()

            if not ret:
                print("Error: Failed to capture a frame.")
                break

            # Display the frame
            cv2.imshow("Camera", frame)

            # Break the loop if the 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the camera and close the OpenCV window
        cap.release()
        cv2.destroyAllWindows()
ft.app(target=main)
