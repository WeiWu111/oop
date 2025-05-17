from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, brand, wholesale_price, retail_price):
        self.brand = brand
        self.wholesale_price = float(wholesale_price)
        self.retail_price = float(retail_price)

    @abstractmethod
    def duplicate(self):
        pass

    @abstractmethod
    def to_csv(self):
        pass

    @abstractmethod
    def display(self):
        pass

    @staticmethod
    @abstractmethod
    def from_csv(fields):
        pass



class Pen(Item, ABC):
    def __init__(self, brand, wholesale_price, retail_price, pen_type):
        super().__init__(brand, wholesale_price, retail_price)
        self.pen_type = pen_type

    @abstractmethod
    def duplicate(self):
        pass

    def to_csv_base(self):
      
        return f"ITEM,{self.brand},PEN,{self.pen_type}"

    def display_base(self):
        return f"{self.brand} {self.pen_type} pen"


class DipPen(Pen):
    def __init__(self, brand, wholesale_price, retail_price, handle_material, handle_color,
                 nib_material, nib_size, nib_shape, nib_color):
        super().__init__(brand, wholesale_price, retail_price, "dip")
        self.handle_material = handle_material
        self.handle_color = handle_color
        self.nib_material = nib_material
        self.nib_size = nib_size
        self.nib_shape = nib_shape
        self.nib_color = nib_color

    def duplicate(self):
        return DipPen(self.brand, self.wholesale_price, self.retail_price,
                      self.handle_material, self.handle_color,
                      self.nib_material, self.nib_size, self.nib_shape, self.nib_color)

    def to_csv(self):
        base = self.to_csv_base()
        return (f"{base},HANDLE,{self.handle_material},{self.handle_color},"
                f"NIB,{self.nib_material},{self.nib_size},{self.nib_shape},{self.nib_color},"
                f"{self.wholesale_price},{self.retail_price}")

    def display(self):
        return (f"{self.brand} dip pen with {self.handle_color} {self.handle_material} handle "
                f"and {self.nib_size} {self.nib_shape} {self.nib_material} nib in {self.nib_color}, "
                f"wholesale ${self.wholesale_price:.2f}, retail ${self.retail_price:.2f}")

    @staticmethod
    def from_csv(fields):
        
        # ITEM,Hakea,PEN,dip,HANDLE,wood,brown,NIB,glass,medium,twisted,blue,16.40,19.30
        if len(fields) < 14:
            raise ValueError("Invalid CSV for DipPen")
        _, brand, _, pen_type, _, handle_material, handle_color, _, nib_material, nib_size, nib_shape, nib_color, wholesale, retail = fields[:14]
        return DipPen(brand, wholesale, retail, handle_material, handle_color, nib_material, nib_size, nib_shape, nib_color)


class FountainPen(Pen):
    def __init__(self, brand, wholesale_price, retail_price, barrel_color, cap_color,
                 nib_material, nib_size, nib_shape, ink_color, ink_type):
        super().__init__(brand, wholesale_price, retail_price, "fountain")
        self.barrel_color = barrel_color
        self.cap_color = cap_color
        self.nib_material = nib_material
        self.nib_size = nib_size
        self.nib_shape = nib_shape
        self.ink_color = ink_color
        self.ink_type = ink_type  

    def duplicate(self):
        return FountainPen(self.brand, self.wholesale_price, self.retail_price,
                           self.barrel_color, self.cap_color,
                           self.nib_material, self.nib_size, self.nib_shape,
                           self.ink_color, self.ink_type)

    def to_csv(self):
        base = self.to_csv_base()
        return (f"{base},{self.barrel_color},{self.cap_color},NIB,{self.nib_material},{self.nib_size},"
                f"{self.nib_shape},INK,cartridge,{self.ink_type},{self.ink_color},"
                f"{self.wholesale_price},{self.retail_price}")

    def display(self):
        return (f"{self.brand} fountain pen with {self.barrel_color} barrel, {self.cap_color} cap, "
                f"{self.nib_size} {self.nib_shape} {self.nib_material} nib, "
                f"{self.ink_color} {self.ink_type} ink, wholesale ${self.wholesale_price:.2f}, retail ${self.retail_price:.2f}")

    @staticmethod
    def from_csv(fields):
        
       
        raise NotImplementedError("FountainPen CSV parsing not implemented in this demo")


class ArtistPen(Pen):
    def __init__(self, brand, wholesale_price, retail_price, pen_tip_types, ink_color):
        super().__init__(brand, wholesale_price, retail_price, "artist")
        
        self.pen_tip_types = pen_tip_types
        self.ink_color = ink_color

    def duplicate(self):
        return ArtistPen(self.brand, self.wholesale_price, self.retail_price,
                         self.pen_tip_types[:], self.ink_color)

    def to_csv(self):
        base = self.to_csv_base()
        tips_str = ",".join(self.pen_tip_types)
        return f"{base},{tips_str},INK,cartridge,artist,{self.ink_color},{self.wholesale_price},{self.retail_price}"

    def display(self):
        tips = " and ".join(self.pen_tip_types)
        return (f"{self.brand} artist pen with {tips} tips and {self.ink_color} artist ink, "
                f"wholesale ${self.wholesale_price:.2f}, retail ${self.retail_price:.2f}")

    @staticmethod
    def from_csv(fields):
        raise NotImplementedError("ArtistPen CSV parsing not implemented in this demo")



class Ink(Item, ABC):
    def __init__(self, brand, wholesale_price, retail_price, ink_type, ink_color):
        super().__init__(brand, wholesale_price, retail_price)
        self.ink_type = ink_type
        self.ink_color = ink_color


class InkBottle(Ink):
    def __init__(self, brand, wholesale_price, retail_price, ink_type, ink_color, volume, volume_unit):
        super().__init__(brand, wholesale_price, retail_price, ink_type, ink_color)
        self.volume = volume
        self.volume_unit = volume_unit

    def duplicate(self):
        return InkBottle(self.brand, self.wholesale_price, self.retail_price,
                         self.ink_type, self.ink_color, self.volume, self.volume_unit)

    def to_csv(self):
        return (f"ITEM,{self.brand},INK,bottle,{self.ink_type},{self.ink_color},{self.volume},{self.volume_unit},"
                f"{self.wholesale_price},{self.retail_price}")

    def display(self):
        return (f"{self.brand} {self.ink_color} {self.ink_type} ink bottle {self.volume}{self.volume_unit}, "
                f"wholesale ${self.wholesale_price:.2f}, retail ${self.retail_price:.2f}")

    @staticmethod
    def from_csv(fields):
        raise NotImplementedError("InkBottle CSV parsing not implemented in this demo")



class PenAccessory(Item, ABC):
    pass


class PenNib(PenAccessory):
    def __init__(self, brand, wholesale_price, retail_price, material, size, shape, color=None):
        super().__init__(brand, wholesale_price, retail_price)
        self.material = material
        self.size = size
        self.shape = shape
        self.color = color

    def duplicate(self):
        return PenNib(self.brand, self.wholesale_price, self.retail_price,
                      self.material, self.size, self.shape, self.color)

    def to_csv(self):
        base = f"ITEM,{self.brand},NIB,{self.material},{self.size},{self.shape}"
        if self.color:
            base += f",{self.color}"
        base += f",{self.wholesale_price},{self.retail_price}"
        return base

    def display(self):
        color_str = f" {self.color}" if self.color else ""
        return (f"{self.brand} {self.size} {self.shape} {self.material} nib{color_str}, "
                f"wholesale ${self.wholesale_price:.2f}, retail ${self.retail_price:.2f}")

    @staticmethod
    def from_csv(fields):
        raise NotImplementedError("PenNib CSV parsing not implemented in this demo")


class GlassPenNib(PenNib):
    def __init__(self, brand, wholesale_price, retail_price, size, shape, color=None):
        super().__init__(brand, wholesale_price, retail_price, "glass", size, shape, color)

    def duplicate(self):
        return GlassPenNib(self.brand, self.wholesale_price, self.retail_price,
                          self.size, self.shape, self.color)

    def to_csv(self):
        return super().to_csv()

    def display(self):
        return super().display()

    @staticmethod
    def from_csv(fields):
        raise NotImplementedError("GlassPenNib CSV parsing not implemented in this demo")



class PenTip(PenAccessory, ABC):
    pass

class BrushPenTip(PenTip):
    def __init__(self, brand, wholesale_price, retail_price, size, material, firmness):
        super().__init__(brand, wholesale_price, retail_price)
        self.size = size
        self.material = material
        self.firmness = firmness

    def duplicate(self):
        return BrushPenTip(self.brand, self.wholesale_price, self.retail_price,
                          self.size, self.material, self.firmness)

    def to_csv(self):
        return (f"ITEM,{self.brand},PEN TIP,brush,{self.size},{self.material},{self.firmness},"
                f"{self.wholesale_price},{self.retail_price}")

    def display(self):
        return (f"{self.brand} {self.size} {self.material} {self.firmness} brush pen tip, "
                f"wholesale ${self.wholesale_price:.2f}, retail ${self.retail_price:.2f}")

    @staticmethod
    def from_csv(fields):
        raise NotImplementedError("BrushPenTip CSV parsing not implemented in this demo")


class MarkerPenTip(PenTip):
    def __init__(self, brand, wholesale_price, retail_price, shape):
        super().__init__(brand, wholesale_price, retail_price)
        self.shape = shape

    def duplicate(self):
        return MarkerPenTip(self.brand, self.wholesale_price, self.retail_price, self.shape)

    def to_csv(self):
        return f"ITEM,{self.brand},PEN TIP,marker,{self.shape},{self.wholesale_price},{self.retail_price}"

    def display(self):
        return (f"{self.brand} {self.shape} marker pen tip, wholesale ${self.wholesale_price:.2f}, "
                f"retail ${self.retail_price:.2f}")

    @staticmethod
    def from_csv(fields):
        raise NotImplementedError("MarkerPenTip CSV parsing not implemented in this demo")


class PenSet(Item):
    def __init__(self, brand, wholesale_price, retail_price, pens):
        super().__init__(brand, wholesale_price, retail_price)
        self.pens = pens 

    def duplicate(self):
        return PenSet(self.brand, self.wholesale_price, self.retail_price,
                      [pen.duplicate() for pen in self.pens])

    def to_csv(self):
        
        return f"ITEM,{self.brand},PEN SET,{len(self.pens)},{self.wholesale_price},{self.retail_price}"

    def display(self):
        return (f"{self.brand} pen set with {len(self.pens)} pens, wholesale ${self.wholesale_price:.2f}, "
                f"retail ${self.retail_price:.2f}")

    @staticmethod
    def from_csv(fields):
        raise NotImplementedError("PenSet CSV parsing not implemented in this demo")


class Page(Item, ABC):
    pass


class PageRefill(Page, ABC):
    pass


class Notebook(Page):
    def __init__(self, brand, wholesale_price, retail_price, size, spine_binding, orientation,
                 cover_material, cover_color, page_design, page_color, num_pages):
        super().__init__(brand, wholesale_price, retail_price)
        self.size = size
        self.spine_binding = spine_binding
        self.orientation = orientation
        self.cover_material = cover_material
        self.cover_color = cover_color
        self.page_design = page_design
        self.page_color = page_color if page_color else "white"
        self.num_pages = int(num_pages)

    def duplicate(self):
        return Notebook(self.brand, self.wholesale_price, self.retail_price,
                        self.size, self.spine_binding, self.orientation,
                        self.cover_material, self.cover_color,
                        self.page_design, self.page_color, self.num_pages)

    def to_csv(self):
        return (f"ITEM,{self.brand},NOTEBOOK,{self.size},{self.spine_binding},{self.orientation},"
                f"{self.cover_material},{self.cover_color},{self.page_design},{self.page_color},"
                f"{self.num_pages},{self.wholesale_price},{self.retail_price}")

    def display(self):
        return (f"{self.brand} {self.size} {self.num_pages} page {self.spine_binding} "
                f"{self.orientation} notebook with {self.page_color} {self.page_design} page "
                f"and {self.cover_color} {self.cover_material} cover, "
                f"wholesale ${self.wholesale_price:.2f}, retail ${self.retail_price:.2f}")

    @staticmethod
    def from_csv(fields):
        raise NotImplementedError("Notebook CSV parsing not implemented in this demo")


class NotebookPageRefill(PageRefill):
    def __init__(self, brand, wholesale_price, retail_price, size, spine_binding, orientation,
                 page_design, page_color, num_pages):
        super().__init__(brand, wholesale_price, retail_price)
        self.size = size
        self.spine_binding = spine_binding
        self.orientation = orientation
        self.page_design = page_design
        self.page_color = page_color if page_color else "white"
        self.num_pages = int(num_pages)

    def duplicate(self):
        return NotebookPageRefill(self.brand, self.wholesale_price, self.retail_price,
                                 self.size, self.spine_binding, self.orientation,
                                 self.page_design, self.page_color, self.num_pages)

    def to_csv(self):
        return (f"ITEM,{self.brand},NOTEBOOK PAGE REFILL,{self.size},{self.spine_binding},{self.orientation},"
                f"{self.page_design},{self.page_color},{self.num_pages},{self.wholesale_price},{self.retail_price}")

    def display(self):
        return (f"{self.brand} {self.size} {self.num_pages} page {self.page_color} {self.page_design} "
                f"refill for {self.orientation} {self.spine_binding} notebook, wholesale ${self.wholesale_price:.2f}, "
                f"retail ${self.retail_price:.2f}")

    @staticmethod
    def from_csv(fields):
        raise NotImplementedError("NotebookPageRefill CSV parsing not implemented in this demo")


class NotebookDivider(PageRefill):
    def __init__(self, brand, wholesale_price, retail_price, num_dividers, color,
                 num_pockets, orientation, spine_binding):
        super().__init__(brand, wholesale_price, retail_price)
        self.num_dividers = int(num_dividers)
        self.color = color
        self.num_pockets = int(num_pockets)
        self.orientation = orientation
        self.spine_binding = spine_binding

    def duplicate(self):
        return NotebookDivider(self.brand, self.wholesale_price, self.retail_price,
                              self.num_dividers, self.color, self.num_pockets,
                              self.orientation, self.spine_binding)

    def to_csv(self):
        return (f"ITEM,{self.brand},NOTEBOOK DIVIDER,{self.num_dividers},{self.color},"
                f"{self.num_pockets},{self.orientation},{self.spine_binding},"
                f"{self.wholesale_price},{self.retail_price}")

    def display(self):
        return (f"{self.brand} {self.num_dividers} {self.color} {self.num_pockets} pocket divider for "
                f"{self.orientation} {self.spine_binding} notebook, wholesale ${self.wholesale_price:.2f}, "
                f"retail ${self.retail_price:.2f}")

    @staticmethod
    def from_csv(fields):
        raise NotImplementedError("NotebookDivider CSV parsing not implemented in this demo")


class Sketchbook(Page):
    def __init__(self, brand, wholesale_price, retail_price, size, orientation,
                 page_weight, texture, page_color, num_pages, cover_material, cover_color):
        super().__init__(brand, wholesale_price, retail_price)
        self.size = size
        self.orientation = orientation
        self.page_weight = page_weight
        self.texture = texture
        self.page_color = page_color if page_color else "white"
        self.num_pages = int(num_pages)
        self.cover_material = cover_material
        self.cover_color = cover_color

    def duplicate(self):
        return Sketchbook(self.brand, self.wholesale_price, self.retail_price,
                         self.size, self.orientation, self.page_weight, self.texture,
                         self.page_color, self.num_pages, self.cover_material, self.cover_color)

    def to_csv(self):
        return (f"ITEM,{self.brand},SKETCHBOOK,{self.size},{self.orientation},{self.page_weight},{self.texture},"
                f"{self.page_color},{self.num_pages},{self.cover_material},{self.cover_color},"
                f"{self.wholesale_price},{self.retail_price}")

    def display(self):
        return (f"{self.brand} {self.size} {self.num_pages} page {self.orientation} sketchbook with "
                f"{self.page_color} {self.texture} {self.page_weight} paper and "
                f"{self.cover_color} {self.cover_material} cover, "
                f"wholesale ${self.wholesale_price:.2f}, retail ${self.retail_price:.2f}")

    @staticmethod
    def from_csv(fields):
        raise NotImplementedError("Sketchbook CSV parsing not implemented in this demo")

class SketchbookPageRefill(PageRefill):
    def __init__(self, brand, wholesale_price, retail_price, size, page_color,
                 page_weight, texture, num_pages, orientation):
        super().__init__(brand, wholesale_price, retail_price)
        self.size = size
        self.page_color = page_color if page_color else "white"
        self.page_weight = page_weight
        self.texture = texture
        self.num_pages = int(num_pages)
        self.orientation = orientation

    def duplicate(self):
        return SketchbookPageRefill(self.brand, self.wholesale_price, self.retail_price,
                                   self.size, self.page_color, self.page_weight,
                                   self.texture, self.num_pages, self.orientation)

    def to_csv(self):
        return (f"ITEM,{self.brand},SKETCHBOOK PAGE REFILL,{self.size},{self.page_color},"
                f"{self.page_weight},{self.texture},{self.num_pages},{self.orientation},"
                f"{self.wholesale_price},{self.retail_price}")

    def display(self):
        return (f"{self.brand} {self.size} {self.num_pages} page {self.page_color} {self.page_weight} "
                f"{self.texture} refill for {self.orientation} sketchbook, wholesale ${self.wholesale_price:.2f}, "
                f"retail ${self.retail_price:.2f}")

    @staticmethod
    def from_csv(fields):
        raise NotImplementedError("SketchbookPageRefill CSV parsing not implemented in this demo")
