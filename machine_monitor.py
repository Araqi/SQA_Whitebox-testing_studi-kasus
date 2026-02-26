class MachineMonitor:

    def __init__(self, machine_id, age_years):
        self.machine_id = machine_id
        self.age_years = age_years

    def validate_production(self, produced, defect, runtime):
        if produced < 0:
            return False
        if defect > produced:
            return False
        if runtime == 0 and produced > 0:
            return False
        return True
        
    def calculate_efficiency(self, produced, defect):
        if produced == 0:
            return 0    
        good = produced - defect
        efficiency = good / produced
        if efficiency >= 0.95:
            return "SANGAT_BAIK"
        elif efficiency >= 0.85:
            return "BAIK"
        elif efficiency >= 0.70:
            return "CUKUP"
        else:
            return "BURUK"
        
    def machine_status(self, downtime):
        if downtime == 0:
            return "OPTIMAL"
        elif downtime < 60:
            return "NORMAL"
        elif downtime < 180:
            return "PERLU_PERHATIAN"
        else:
            return "KRITIS"
        
    def risk_detection(self, temperature, downtime):
        if temperature > 90 and self.age_years > 10 and downtime > 120:
            return "HIGH_RISK"
        if temperature > 80 and downtime > 60:
            return "MEDIUM_RISK"
        return "LOW_RISK"