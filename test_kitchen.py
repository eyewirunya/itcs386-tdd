
from kitchen import Quantity
from kitchen import Converter
from kitchen import grams
from kitchen import ounces





def test_multiplication():
    flour = grams(200)
    assert flour.times(3) == grams(600)

    




def test_reduce_same_unit_needs_no_rate():
    converter = Converter()
    assert converter.reduce(grams(500), "g") == grams(500)





def test_ounces_to_grams():
    converter = Converter()
    converter.add_rate("oz", "g", 28)

    assert converter.reduce(ounces(2), "g") == grams(56)



