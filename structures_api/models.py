from django.db import models
from django.contrib.gis.db import models as gis_models

from .validators import aup_validator_since, aup_validator_to, reservation_validator_since, reservation_validator_to

AIRSPACE_TYPES = [
    ('TSA', 'TSA'),
    ('TRA', 'TRA'),
    ('EA', 'EA'),
    ('D', 'D'),
    ('R', 'R'),
    ('P', 'P'),
    ('CTR', 'CTR'),
    ('TMA', 'TMA'),
    ('ATZ', 'ATZ'),
    ('MCTR', 'MCTR'),
    ('MTMA', 'MTMA'),
    ('ADIZ', 'ADIZ'),
    ('MRT', 'MRT'),
]

ALTITUDES = [
    ('GND', 'GND'),
    ('A005', 'A005'),
    ('A015', 'A015'),
    ('A025', 'A025'),
    ('A035', 'A035'),
    ('A045', 'A045'),
    ('A055', 'A055'),
    ('A065', 'A065'),
    ('FL85', 'FL85'),
    ('FL95', 'FL95'),
    ('FL105', 'FL105'),
    ('FL115', 'FL115'),
    ('FL125', 'FL125'),
    ('FL135', 'FL135'),
    ('FL145', 'FL145'),
    ('FL155', 'FL155'),
    ('FL165', 'FL165'),
    ('FL175', 'FL175'),
    ('FL185', 'FL185'),
    ('FL195', 'FL195'),
    ('FL205', 'FL205'),
    ('FL215', 'FL215'),
    ('FL225', 'FL225'),
    ('FL235', 'FL235'),
    ('FL245', 'FL245'),
    ('FL255', 'FL255'),
    ('FL265', 'FL265'),
    ('FL275', 'FL275'),
    ('FL285', 'FL285'),
    ('FL295', 'FL295'),
    ('FL305', 'FL305'),
    ('FL315', 'FL315'),
    ('FL325', 'FL325'),
    ('FL335', 'FL335'),
    ('FL345', 'FL345'),
    ('FL355', 'FL355'),
    ('FL365', 'FL365'),
    ('FL375', 'FL375'),
    ('FL385', 'FL385'),
    ('FL395', 'FL395'),
    ('FL405', 'FL405'),
    ('FL415', 'FL415'),
    ('FL425', 'FL425'),
    ('FL435', 'FL435'),
    ('FL445', 'FL445'),
    ('FL455', 'FL455'),
    ('FL465', 'FL465'),
    ('FL475', 'FL475'),
    ('FL485', 'FL485'),
    ('FL495', 'FL495'),
    ('FL505', 'FL505'),
    ('FL515', 'FL515'),
    ('FL525', 'FL525'),
    ('FL535', 'FL535'),
    ('FL545', 'FL545'),
    ('FL555', 'FL555'),
    ('FL565', 'FL565'),
    ('FL575', 'FL575'),
    ('FL585', 'FL585'),
    ('FL595', 'FL595'),
    ('FL605', 'FL605'),
    ('FL615', 'FL615'),
    ('FL625', 'FL625'),
    ('FL635', 'FL635'),
    ('FL645', 'FL645'),
    ('FL655', 'FL655'),
    ('FL660', 'FL660'),
]


class AirspaceStructure(gis_models.Model):
    name = gis_models.CharField(max_length=30)
    airspace_type = gis_models.CharField(max_length=5, choices=AIRSPACE_TYPES)
    lower_limit = gis_models.CharField(max_length=5, choices=ALTITUDES)
    upper_limit = gis_models.CharField(max_length=5, choices=ALTITUDES)
    localization = gis_models.PolygonField()

    def __str__(self):
        return f"Name: {self.name}, type: {self.airspace_type}"


class Reservation(models.Model):
    airspace_structure = models.ForeignKey(AirspaceStructure, on_delete=models.CASCADE)
    lower_limit = models.CharField(max_length=5, choices=ALTITUDES)
    upper_limit = models.CharField(max_length=5, choices=ALTITUDES)
    activation_date = models.DateField(validators=[reservation_validator_since])
    deactivation_date = models.DateField(validators=[reservation_validator_to])
    activation_time = models.TimeField()
    deactivation_time = models.TimeField()

    def __str__(self):
        return f"""
                Reservation on: {self.airspace_structure}
                Altitude lower limit: {self.lower_limit}
                Altitude upper limit: {self.upper_limit}
                Activation at: {self.activation_time}
                Deactivation at: {self.deactivation_time}
                """

    class Meta:
        permissions = [
            ("request_tsa", "Can request TSA type airspace"),
            ("request_tra", "Can request TRA type airspace"),
            ("request_ea", "Can request EA type airspace"),
            ("request_atz", "Can request ATZ type airspace"),
            ("request_mrt", "Can request MRT type airspace"),
        ]


class Aup(models.Model):
    creation_time = models.DateTimeField(auto_now_add=True)
    validity_time_since = models.DateField(validators=[aup_validator_since])
    validity_time_to = models.DateField(validators=[aup_validator_to])
    requests = models.ManyToManyField(Reservation)
