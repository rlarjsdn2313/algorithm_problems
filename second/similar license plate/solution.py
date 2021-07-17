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

        
        parking_lots.append({'k': k, 'parking_lot': license_plates})

    return parking_lots

print(get_problem())