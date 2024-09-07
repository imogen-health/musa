from app.repositories.educational_campaigns_service_offers import (
    get_educational_campaigns_service_offers,
)
from app.repositories.educational_service_offers import get_educational_service_offers
from app.repositories.protection_service_offers import get_protection_service_offers
from app.repositories.public_service_offers import get_public_service_offers


class ServiceOffersRepository(object):
    def get_service_offers(self):
        return [
            get_public_service_offers(),
            get_protection_service_offers(),
            get_educational_service_offers(),
            get_educational_campaigns_service_offers(),
        ]
