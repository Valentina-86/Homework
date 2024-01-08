from string_utils import StringUtils

string_utils = StringUtils()

def test_capitilize():
    string_utils = StringUtils()
    res = string_utils.capitilize("skypro")
    assert res == "Skypro"

def test_trim():
    string_utils = StringUtils()
    res = string_utils.trim(" skypro")
    assert res == "skypro"
    
def test_to_list():
    string_utils = StringUtils()
    res = string_utils.to_list("a,b,c,d")
    assert res == ["a", "b", "c", "d"]
        
def test_to_list():
    string_utils = StringUtils()
    res = string_utils.to_list("1:2:3", ":")
    assert res == ["1", "2", "3"]
     
def test_contains():
    string_utils = StringUtils()
    res = string_utils.contains("SkyPro", "S")
    assert res == True
            
def test_contains():
    string_utils = StringUtils()
    res = string_utils.contains("SkyPro", "U")
    assert res == False
                
def test_delete_symbol():
    string_utils = StringUtils()
    res = string_utils.delete_symbol("SkyPro", "k")
    assert res == "SyPro"
                    
def test_delete_symbol():
    string_utils = StringUtils()
    res = string_utils.delete_symbol("SkyPro", "Pro")
    assert res == "Sky"
           
def test_starts_with():
    string_utils = StringUtils()
    res = string_utils.starts_with("SkyPro", "S")
    assert res == True
            
def test_starts_with():
    string_utils = StringUtils()
    res = string_utils.starts_with("SkyPro", "P")
    assert res == False
               
def test_end_with():
    string_utils = StringUtils()
    res = string_utils.end_with("SkyPro", "o")
    assert res == True
            
def test_end_with():
    string_utils = StringUtils()
    res = string_utils.end_with("SkyPro", "y")
    assert res == False
                   
def test_is_empty():
    string_utils = StringUtils()
    res = string_utils.is_empty("")
    assert res == True
                       
def test_is_empty():
    string_utils = StringUtils()
    res = string_utils.is_empty(" ")
    assert res == True
            
def test_is_emptyh():
    string_utils = StringUtils()
    res = string_utils.is_empty("SkyPro")
    assert res == False
                       
def test_list_to_string():
    string_utils = StringUtils()
    res = string_utils.list_to_string([1,2,3,4])
    assert res == "1, 2, 3, 4"
                       
def test_list_to_string():
    string_utils = StringUtils()
    res = string_utils.list_to_string(["Sky", "Pro"])
    assert res == "Sky, Pro"
            
def test_list_to_string():
    string_utils = StringUtils()
    res = string_utils.list_to_string(["Sky", "Pro"], "-")
    assert res == "Sky-Pro"