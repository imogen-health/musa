class ServiceOfferGroup(object):
    def __init__(self, name, service_offers):
        self.__name = name
        self.__service_offers = service_offers

    @property
    def name(self):
        return self.__name

    @property
    def service_offers(self):
        return self.__service_offers
