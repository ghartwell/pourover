# pylint: disable=C0103, C0301, E1101, W1306
"""
Make JSON API for calculating the water and coffee in grams for pour over
"""

from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

waterToCoffeeRatio = 20


def coffee_math(coffee_g):
    water_g = coffee_g * waterToCoffeeRatio
    return water_g, coffee_g


def water_math(water_oz):
    water_g = 29.57 * water_oz
    coffee_g = water_g / waterToCoffeeRatio
    return water_g, coffee_g


class PourOver(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("water", type=int, required=False, help="Water in fluid ounces.")
        parser.add_argument("coffee", type=int, required=False, help="Coffee in grams.")
        args = parser.parse_args()

        water_g = "NA"
        coffee_g = "NA"

        if args["water"] and args["coffee"]:
            pass
        elif args["water"]:
            water_g, coffee_g = water_math(args["water"])
        elif args["coffee"]:
            water_g, coffee_g = coffee_math(args["coffee"])
        else:
            pass

        coffee = {"water grams": water_g, "coffee grams": coffee_g}

        return coffee, 200


api.add_resource(PourOver, "/pourover")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
