import unittest
from machine_monitor import MachineMonitor

class TestMachineMonitorDeep(unittest.TestCase):

    def setUp(self):
        self.m_new = MachineMonitor("NEW", 5)
        self.m_old = MachineMonitor("OLD", 15)

    def test_validate_production_logic(self):
        self.assertFalse(self.m_new.validate_production(-1, 0, 10))  
        self.assertTrue(self.m_new.validate_production(0, 0, 0))    
        self.assertFalse(self.m_new.validate_production(10, 11, 10)) 
        self.assertTrue(self.m_new.validate_production(10, 10, 10))  
        self.assertFalse(self.m_new.validate_production(10, 2, 0))  
        self.assertTrue(self.m_new.validate_production(10, 2, 1))    

    def test_calculate_efficiency_logic(self):
        self.assertEqual(self.m_new.calculate_efficiency(0, 0), 0)           
        self.assertEqual(self.m_new.calculate_efficiency(100, 5), "SANGAT_BAIK") 
        self.assertEqual(self.m_new.calculate_efficiency(100, 4), "SANGAT_BAIK") 
        self.assertEqual(self.m_new.calculate_efficiency(100, 15), "BAIK")       
        self.assertEqual(self.m_new.calculate_efficiency(100, 10), "BAIK")       
        self.assertEqual(self.m_new.calculate_efficiency(100, 30), "CUKUP")    
        self.assertEqual(self.m_new.calculate_efficiency(100, 20), "CUKUP")   
        self.assertEqual(self.m_new.calculate_efficiency(100, 31), "BURUK")   

    def test_machine_status_logic(self):
        self.assertEqual(self.m_new.machine_status(0), "OPTIMAL")            
        self.assertEqual(self.m_new.machine_status(59), "NORMAL")            
        self.assertEqual(self.m_new.machine_status(60), "PERLU_PERHATIAN") 
        self.assertEqual(self.m_new.machine_status(179), "PERLU_PERHATIAN")  
        self.assertEqual(self.m_new.machine_status(180), "KRITIS")           

    def test_risk_detection_logic(self):
        self.assertEqual(self.m_old.risk_detection(91, 121), "HIGH_RISK")   
        self.assertEqual(self.m_new.risk_detection(91, 121), "MEDIUM_RISK") 
        self.assertEqual(self.m_old.risk_detection(81, 61), "MEDIUM_RISK")  
        self.assertEqual(self.m_new.risk_detection(70, 30), "LOW_RISK")     

if __name__ == '__main__':
    unittest.main()