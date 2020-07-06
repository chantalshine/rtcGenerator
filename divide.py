finalGroup = []

from google.cloud import storage


def check(group, check):
    count =0
    for i in group:
        for j in i:
            if check in j:
                count += 1

    return count




#problem 4: base cases of small groups
#problem 3: did not reinitialize array when I needed to
def divide3(group):
    finalGroup=[]
    if len(group) ==0:
        return []
    if len(group) ==1:
        finalGroup.append(group[0])
        return finalGroup
    if len(group) ==2:
        finalGroup.append(group[0])
        finalGroup.append(group[1])
        return finalGroup
    if len(group) ==3:
        finalGroup.append(group[0])
        finalGroup.append(group[1])
        finalGroup.append(group[2])
        return finalGroup
    # divdes filtered groups into 3 and returns 1 list of lists of 3
    subGroupThree = []
    limit = 0
    for i in range(len(group)):
        if limit == 3:
            limit = 0
            finalGroup.append(subGroupThree)
            subGroupThree = []
            subGroupThree.append(group[i])
            limit += 1
            continue
        else:
            if i == len(group) - 1 :
                limit = 0
                finalGroup.append(subGroupThree)
                subGroupThree = []
                continue
            subGroupThree.append(group[i])
            limit += 1

    return finalGroup


# Problem 2 was 'Sunday Morning was not one el, it was concatenated with other days/times

def daysEastSun(eastern, days):
    easternSun = []
    getRidOf = []

    for i in eastern:
        for j in i:
            if (days + " morning") in j \
                    or (days + " afternoon") in j \
                    or (days + " evening") in j:
                getRidOf.append(i)
                easternSun.append(i)

    for i in range(len(getRidOf)):
        eastern.remove(getRidOf[i])

    return easternSun


def uploadCloud():
    storage_client = storage.Client()
    # The name for the new bucket
    bucket_name = "my-new-bucket"

    # Creates the new bucket
    bucket = storage_client.create_bucket(bucket_name)

    print("Bucket {} created.".format(bucket.name))

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob("groupFile")
    blob.upload_from_filename('groups.txt')
    print("File {} uploaded to {}.".format('groups.txt', 'groupFile'))
