import uuid
nameko.rpc import rpc
nameko_redis import Redis


class AirportService:
    name ="trip_service"
    redis = Redis('development')
    @rpc

    def get(self,trip_id):
        trip = get.redis.get(trip_id)

        return trip


    @rpc
    def create(self, airport_to_id,aiport_from_id):
        trip_id =uuid.uuid4().hex
         self.redis.set(trip_id,{
             "from":aiport_from_id
             "to":airport_to_id
         })
        return trip_id





