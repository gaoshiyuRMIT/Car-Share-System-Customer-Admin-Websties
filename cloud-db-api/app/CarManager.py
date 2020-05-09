import pymysql as _p
from .DBManager import DBManager


class CarManager(DBManager):
    FIELDS = ["car_id", "year", "car_model", "body_type", "num_seats", 
                "car_colour", "cost_hour", "latitude", "longitude", "car_status"]
    TABLE_NAME = "Car"


    def getMany(self, filt: dict) -> list:
        return super().getMany(filt)
    
    def updateOne(self, car_id, car: dict) -> bool:
        if len(car) == 0:
            return False
        success = False
        if list(car.keys()) == ["car_status"]:
            car_status = car["car_status"]
            sql = "UPDATE " + self.TABLE_NAME + " SET car_status = %s WHERE car_id = %s"
            conn = self.conn
            try:
                with conn.cursor() as cursor:
                    done = cursor.execute(sql, (car_status, car_id,))
                    conn.commit()
                success = done == 1
            except (_p.OperationalError, _p.InternalError, _p.NotSupportedError): #errors related to db functioning
                # "Internal Database error"
                conn.rollback()
                raise
            except _p.ProgrammingError:
                #error related to sql syntax etc
                conn.rollback()
                raise
            except _p.IntegrityError:
                #issue related to integrity of db 
                conn.rollback()
                raise
            except:
                conn.rollback()
                raise # unkown error type
        else:
            raise NotImplementedError
        return success

    def getOne(self, carId) -> dict:
        sql = "SELECT * FROM " + self.TABLE_NAME + " WHERE car_id = %s"
        conn = self.conn
        try:
            with self.getCursor(conn) as cursor:
                cursor.execute(sql, (carId,))
                return cursor.fetchall()
        except (_p.OperationalError, _p.InternalError, _p.NotSupportedError): #errors related to db functioning
            # "Internal Database error"
            raise
        except _p.ProgrammingError:
            #error rrelated to sql syntax etc
            raise
        except:
            raise
        

    def addOne(self, car: dict):
        # returns carId
        return 0             