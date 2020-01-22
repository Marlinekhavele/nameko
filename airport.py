import uuid
nameko.rpc import rpc
nameko_redis import Redis


class AirportService:
    name = "airport_service"

    redis = Redis('development')


    @rpc
    def get(self,airport_id):
        airport = self.redis.get(airport_id)
        return airport


    @rpc
    def create(self,aiport):
        airport_id = uuid.uuid4().hex
        self.redis.set(airport_id,aiport)
        return airport_id


