import unittest
import src.registration_service as srvc

class test_registration(unittest.TestCase):

    def test_valid_registration(self):
        
        valid, msg = srvc.register("AZAZAZAZAZ_8", "абвгдежН7_", "абвгдежН7_")
        self.assertTrue(valid)

    def test_registration_with_wrong_Login(self):
        
        valid, msg =  srvc.register("AZAZAуййуйуZAZAZ_8","абвгдежН7_","абвгдежН7_")
        self.assertFalse(valid)
    def test_registration_with_wrong_Password_repeat(self):
        
        valid, msg = srvc.register("AZAZAZAZAZ_8", "абвгдежН7_", "абвгдежqq7_")
        self.assertFalse(valid)

    def test_registration_with_wrong_password_len(self):
        
        valid, msg = srvc.register("AZAZAZAZAZ_8", "аВб7_", "аВб7_")
        self.assertFalse(valid)
    def test_registration_pass_without_special_symbol(self):
        
        valid, msg = srvc.register("AZAZAZAZAZ_8", "абвгдежН7", "абвгдежН7")
        self.assertFalse(valid)

    def test_registration_pass_without_num_symbol(self):
        
        valid, msg = srvc.register("AZAZAZAZAZ_8", "абвгдежН_", "абвгдежН_")
        self.assertFalse(valid)

    def test_registration_pass_non_cyrilic_symbol(self):
        
        valid, msg = srvc.register("AZAZAZAZAZ_8", "аahujaujakaН_", "аahujaujakaН_")
        self.assertFalse(valid)

    def test_registration_pass_upper_case(self):
        
        valid, msg = srvc.register("AZAZAZAZAZ_8", "абвгдежН7_".upper(), "абвгдежН7_".upper())
        self.assertFalse(valid)

    def test_registration_pass_lower_case(self):
        
        valid, msg = srvc.register("AZAZAZAZAZ_8", "абвгдежН7_".lower(), "абвгдежН7_".lower())
        self.assertFalse(valid)

    def test_registration_login_in_blocked_list(self):
        
        valid, msg = srvc.register("redsusik228", "абвгдежН7_", "абвгдежН7_")
        self.assertFalse(valid)
    def test_registration_login_in_blocked_list2(self):
        
        valid, msg = srvc.register("adminboss42", "абвгдежН7_", "абвгдежН7_")
        self.assertFalse(valid)
    def test_registration_login_invalid_len(self):
        
        valid, msg = srvc.register("admi", "абвгдежН7_", "абвгдежН7_")
        self.assertFalse(valid)
    def test_valid_mail_registration(self):
        
        valid, msg = srvc.register("example@da.com", "абвгдежН7_", "абвгдежН7_")
        self.assertTrue(valid)
    def test_valid_num_registration(self):
        
        valid, msg = srvc.register("+7 777 777 77 77", "абвгдежН7_", "абвгдежН7_")
        self.assertTrue(valid)
    def test_invalid_num_registration(self):
        
        valid, msg = srvc.register("+7 777 777 77999999 77", "абвгдежН7_", "абвгдежН7_")
        self.assertFalse(valid)
    def test_invalid_mail_registration(self):
        
        valid, msg = srvc.register("exampleda.com", "абвгдежН7_", "абвгдежН7_")
        self.assertFalse(valid)
    def test_invalid_login_registration(self):
        
        valid, msg = srvc.register("дадаадда8&", "абвгдежН7_", "абвгдежН7_")
        self.assertFalse(valid)

    def test_invalid_login_without_num_registration(self):
        
        valid, msg = srvc.register("nmananan&", "абвгдежН7_", "абвгдежН7_")
        self.assertFalse(valid)

    def test_invalid_login_without_special_symbol_registration(self):
        
        valid, msg = srvc.register("nmananan8", "абвгдежН7_", "абвгдежН7_")
        self.assertFalse(valid)

    def test_invalid_login_without_special_symbol__registration(self):
        
        valid, msg = srvc.register("nmananan8&", "абвгдежН7_", "абвгдежН7_")
        self.assertFalse(valid)

if __name__ == '__main__':
    unittest.main()
