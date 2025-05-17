class Pen(Item):
    @staticmethod
    def from_csv(fields):
        if len(fields) < 6:
            raise ValueError("Invalid CSV for Pen")
        brand = fields[1]
        pen_type = fields[3]
        wholesale_price = float(fields[-2])
        retail_price = float(fields[-1])
        return Pen(brand, wholesale_price, retail_price, pen_type)

class DipPen(Pen):
    @staticmethod
    def from_csv(fields):
        if len(fields) < 14:
            raise ValueError("Invalid CSV for DipPen")
        brand = fields[1]
        handle_material = fields[5]
        handle_color = fields[6]
        nib_material = fields[8]
        nib_size = fields[9]
        nib_shape = fields[10]
        nib_color = fields[11]
        wholesale_price = float(fields[12])
        retail_price = float(fields[13])
        return DipPen(brand, wholesale_price, retail_price,
                      handle_material, handle_color,
                      nib_material, nib_size, nib_shape, nib_color)

class FountainPen(Pen):
    @staticmethod
    def from_csv(fields) :
        if len(fields) < 15:
            raise ValueError("Invalid CSV for FountainPen")
        brand = fields[1]
        barrel_color = fields[4]
        cap_color = fields[5]
        nib_material = fields[7]
        nib_size = fields[8]
        nib_shape = fields[9]
        ink_type = fields[11]
        ink_color = fields[12]
        wholesale_price = float(fields[13])
        retail_price = float(fields[14])
        return FountainPen(brand, wholesale_price, retail_price,
                           barrel_color, cap_color,
                           nib_material, nib_size, nib_shape,
                           ink_color, ink_type)

class ArtistPen(Pen):
    @staticmethod
    def from_csv(fields):
        if len(fields) < 9:
            raise ValueError("Invalid CSV for ArtistPen")
        brand = fields[1]
        tips_str = fields[4]
        pen_tip_types = tips_str.split(';')  
        ink_color = fields[7]
        wholesale_price = float(fields[8])
        retail_price = float(fields[9])
        return ArtistPen(brand, wholesale_price, retail_price, pen_tip_types, ink_color)

class InkCartridge(Item):
    @staticmethod
    def from_csv(fields):
        if len(fields) < 8:
            raise ValueError("Invalid CSV for InkCartridge")
        brand = fields[1]
        ink_type = fields[4]
        ink_color = fields[5]
        wholesale_price = float(fields[6])
        retail_price = float(fields[7])
        return InkCartridge(brand, wholesale_price, retail_price, ink_type, ink_color)

class InkBottle(Ink):
    @staticmethod
    def from_csv(fields):
        if len(fields) < 11:
            raise ValueError("Invalid CSV for InkBottle")
        brand = fields[1]
        ink_type = fields[4]
        ink_color = fields[5]
        volume = float(fields[6])
        volume_unit = fields[7]
        wholesale_price = float(fields[8])
        retail_price = float(fields[9])
        return InkBottle(brand, wholesale_price, retail_price, ink_type, ink_color, volume, volume_unit)

class PenNib(PenAccessory):
    @staticmethod
    def from_csv(fields):
        if len(fields) < 9:
            raise ValueError("Invalid CSV for PenNib")
        brand = fields[1]
        material = fields[3]
        size = fields[4]
        shape = fields[5]
        color = fields[6] if fields[6] != '' else None
        wholesale_price = float(fields[7])
        retail_price = float(fields[8])
        return PenNib(brand, wholesale_price, retail_price, material, size, shape, color)

class GlassPenNib(PenNib):
    @staticmethod
    def from_csv(fields):
        nib = PenNib.from_csv(fields)
        if nib.material.lower() != "glass":
            raise ValueError("GlassPenNib material must be glass")
        return GlassPenNib(nib.brand, nib.wholesale_price, nib.retail_price,
                          nib.size, nib.shape, nib.color)

class BrushPenTip(PenTip):
    @staticmethod
    def from_csv(fields):
        if len(fields) < 9:
            raise ValueError("Invalid CSV for BrushPenTip")
        brand = fields[1]
        size = fields[4]
        material = fields[5]
        firmness = fields[6]
        wholesale_price = float(fields[7])
        retail_price = float(fields[8])
        return BrushPenTip(brand, wholesale_price, retail_price, size, material, firmness)

class MarkerPenTip(PenTip):
    @staticmethod
    def from_csv(fields):
        if len(fields) < 7:
            raise ValueError("Invalid CSV for MarkerPenTip")
        brand = fields[1]
        shape = fields[4]
        wholesale_price = float(fields[5])
        retail_price = float(fields[6])
        return MarkerPenTip(brand, wholesale_price, retail_price, shape)

class PenSet(Item):
    @staticmethod
    def from_csv(fields):
        if len(fields) < 6:
            raise ValueError("Invalid CSV for PenSet")
        brand = fields[1]
        num_pens = int(fields[4])
        wholesale_price = float(fields[5])
        retail_price = float(fields[6])
        return PenSet(brand, wholesale_price, retail_price, pens=[])

class Notebook(Page):
    @staticmethod
    def from_csv(fields):
        if len(fields) < 13:
            raise ValueError("Invalid CSV for Notebook")
        brand = fields[1]
        size = fields[3]
        spine_binding = fields[4]
        orientation = fields[5]
        cover_material = fields[6]
        cover_color = fields[7]
        page_design = fields[8]
        page_color = fields[9] if fields[9] else "white"
        num_pages = int(fields[10])
        wholesale_price = float(fields[11])
        retail_price = float(fields[12])
        return Notebook(brand, wholesale_price, retail_price, size, spine_binding, orientation,
                        cover_material, cover_color, page_design, page_color, num_pages)

class NotebookPageRefill(PageRefill):
    @staticmethod
    def from_csv(fields):
        if len(fields) < 11:
            raise ValueError("Invalid CSV for NotebookPageRefill")
        brand = fields[1]
        size = fields[3]
        spine_binding = fields[4]
        orientation = fields[5]
        page_design = fields[6]
        page_color = fields[7] if fields[7] else "white"
        num_pages = int(fields[8])
        wholesale_price = float(fields[9])
        retail_price = float(fields[10])
        return NotebookPageRefill(brand, wholesale_price, retail_price, size, spine_binding,
                                  orientation, page_design, page_color, num_pages)

class NotebookDivider(PageRefill):
    @staticmethod
    def from_csv(fields):
        if len(fields) < 10:
            raise ValueError("Invalid CSV for NotebookDivider")
        brand = fields[1]
        num_dividers = int(fields[3])
        color = fields[4]
        num_pockets = int(fields[5])
        orientation = fields[6]
        spine_binding = fields[7]
        wholesale_price = float(fields[8])
        retail_price = float(fields[9])
        return NotebookDivider(brand, wholesale_price, retail_price, num_dividers, color,
                               num_pockets, orientation, spine_binding)

class Sketchbook(Page):
    @staticmethod
    def from_csv(fields):
        if len(fields) < 13:
            raise ValueError("Invalid CSV for Sketchbook")
        brand = fields[1]
        size = fields[3]
        orientation = fields[4]
        page_weight = fields[5]
        texture = fields[6]
        page_color = fields[7] if fields[7] else "white"
        num_pages = int(fields[8])
        cover_material = fields[9]
        cover_color = fields[10]
        wholesale_price = float(fields[11])
        retail_price = float(fields[12])
        return Sketchbook(brand, wholesale_price, retail_price, size, orientation,
                         page_weight, texture, page_color, num_pages,
                         cover_material, cover_color)

class SketchbookPageRefill(PageRefill):
    @staticmethod
    def from_csv(fields):
        if len(fields) < 11:
            raise ValueError("Invalid CSV for SketchbookPageRefill")
        brand = fields[1]
        size = fields[3]
        page_color = fields[4] if fields[4] else "white"
        page_weight = fields[5]
        texture = fields[6]
        num_pages = int(fields[7])
        orientation = fields[8]
        wholesale_price = float(fields[9])
        retail_price = float(fields[10])
        return SketchbookPageRefill(brand, wholesale_price, retail_price, size, page_color,
                                    page_weight, texture, num_pages, orientation)
