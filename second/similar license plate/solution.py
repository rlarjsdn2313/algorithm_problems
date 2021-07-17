import string

# alphabet lower cases
SMALL_ALPHA = string.ascii_lowercase

# alphabet upper case
BIG_ALPHA = string.ascii_uppercase


def get_problem():
    # get number of test case
    t = int(input())

    # value for save status of each parking lot
    parking_lots = []


    # get test cases
    for _ in range(t):
        # get how many cars and length of each license plate
        n, k = str(input()).split(' ')

        # make num_of_cars and len_of_license_plate int
        n, k = int(n), int(k)

        # value for save license_plates
        license_plates = str(input()).split(' ')
        
        # add result
        parking_lots.append({'k': k, 'parking_lot': license_plates})

    return parking_lots


def parse_license_plates(license_plates):
    result = []


    for license_plate in license_plates:
        # value for save result of each liecnse_pate
        parsed_license_plate = {
            'license_plate': license_plate, 
            'small': {}, 
            'big': 0
        }

        # low license_plate
        low_license_plate = license_plate.lower()


        for low in SMALL_ALPHA:
            # add each low and count how many in license_plates
            parsed_license_plate['small'][low] = low_license_plate.count(low)

        
        for letter in license_plate:
            if letter in BIG_ALPHA:
                parsed_license_plate['big'] += 1

        result.append(parsed_license_plate)

    return result


def main():
    # get problems
    parking_lots = get_problem()

    result = []

    for parking_lot in parking_lots:
        parsed_license_plates \
            = parse_license_plates(parking_lot['parking_lot'])
        
        count = 0
        i = 0

        for i in range(len(parsed_license_plates)):
            for a in range(i + 1, len(parsed_license_plates)):
                if (parsed_license_plates[i]['big'] == parsed_license_plates[a]['big']\
                    and parsed_license_plates[i]['small'] == parsed_license_plates[a]['small']):
                    count += 1

        result.append(count)

    for a in result:
        print(a)

main()