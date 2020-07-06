import gspread

from oauth2client.service_account import ServiceAccountCredentials
from google.cloud import storage
from divide import divide3
from divide import daysEastSun
from divide import check
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('RTCGroupGenerator-e37820e6141a.json', scope)
client = gspread.authorize(creds)

sheet = client.open('interview_data').sheet1
interviewData = sheet.get_all_values()
senior = []
junior = []
soph = []
fresh = []
# dividing into class years

#makes ense python reads it as fall 2020 (xyz in interview data) OHHHHHHHHHHHHHHHHHH
#x=99
#if 'Fall 2020' in interviewData[1] or 'Spring/Summer 2021' in interviewData[1]:
#    x=100
#print(x )

for i in interviewData:
    if 'Spring/Summer 2021' in i or 'Fall 2020' in i:
        senior.append(i)
        continue
    if 'Fall 2021' in i or 'Spring/Summer 2022' in i:
        junior.append(i)
        continue
    if 'Fall 2022' in i or 'Spring/Summer 2023' in i:
        soph.append(i)
        continue
    if 'Fall 2023' in i:
        fresh.append(i)
        continue

# dividing into time zone
seniorEastern = []
seniorCentral = []
seniorMountain = []
seniorPacific = []

juniorEastern = []
juniorCentral = []
juniorMountain = []
juniorPacific = []


sophEastern = []
sophCentral = []
sophMountain = []
sophPacific = []

freshEastern = []
freshCentral = []
freshMountain = []
freshPacific = []

for i in range(len(senior)):
    if 'Eastern' in senior[i]:
        seniorEastern.append(senior[i])
    if 'Central' in senior[i]:
        seniorCentral.append(senior[i])
    if 'Mountain' in senior[i]:
        seniorMountain.append(senior[i])
    if 'Pacific' in senior[i]:
        seniorPacific.append(senior[i])

for i in range(len(junior)):
    if 'Eastern' in junior[i]:
        juniorEastern.append(junior[i])
    if 'Central' in junior[i]:
        juniorCentral.append(junior[i])
    if 'Mountain' in junior[i]:
        juniorMountain.append(junior[i])
    if 'Pacific' in junior[i]:
        juniorPacific.append(junior[i])

for i in range(len(soph)):
    if 'Eastern' in soph[i]:
        sophEastern.append(soph[i])
    if 'Central' in soph[i]:
        sophCentral.append(soph[i])
    if 'Mountain' in soph[i]:
        sophMountain.append(soph[i])
    if 'Pacific' in soph[i]:
        sophPacific.append(soph[i])

for i in range(len(fresh)):
    if 'Eastern' in fresh[i]:
        freshEastern.append(fresh[i])
    if 'Central' in fresh[i]:
        freshCentral.append(fresh[i])
    if 'Mountain' in fresh[i]:
        freshMountain.append(fresh[i])
    if 'Pacific' in fresh[i]:
        freshPacific.append(fresh[i])

seniorEastData =[]
seniorEastPM =[]
seniorEastUI=[]
seniorEastQ=[]
seniorCentData =[]
seniorCentPM =[]
seniorCentUI=[]
seniorCentQ=[]
seniorMountData =[]
seniorMountPM =[]
seniorMountUI=[]
seniorMountQ=[]
seniorPacData =[]
seniorPacPM =[]
seniorPacUI=[]
seniorPacQ=[]


jEastData =[]
jEastPM =[]
jEastUI=[]
jEastQ=[]
jCentData =[]
jCentPM =[]
jCentUI=[]
jCentQ=[]
jMountData =[]
jMountPM =[]
jMountUI=[]
jMountQ=[]
jPacData =[]
jPacPM =[]
jPacUI=[]
jPacQ=[]

soEastData =[]
soEastPM =[]
soEastUI=[]
soEastQ=[]
soCentData =[]
soCentPM =[]
soCentUI=[]
soCentQ=[]
soMountData =[]
soMountPM =[]
soMountUI=[]
soMountQ=[]
soPacData =[]
soPacPM =[]
soPacUI=[]
soPacQ=[]

frEastData =[]
frEastPM =[]
frEastUI=[]
frEastQ=[]
frCentData =[]
frCentPM =[]
frCentUI=[]
frCentQ=[]
frMountData =[]
frMountPM =[]
frMountUI=[]
frMountQ=[]
frPacData =[]
frPacPM =[]
frPacUI=[]
frPacQ=[]

for i in seniorEastern:
    for j in i:
        if 'Data Science' in j:
            seniorEastData.append(i)
        if 'Product Management' in j:
            seniorEastPM.append(i)
        if 'Software Engineering' in j:
            seniorEastUI.append(i)
        if 'Quantitative Development/Quantitative Research' in j:
            seniorEastQ.append(i)

for i in seniorCentral:
    for j in i:
        if 'Data Science' in j:
            seniorCentData.append(i)
        if 'Product Management' in j:
            seniorCentPM.append(i)
        if 'Software Engineering' in j:
            seniorCentUI.append(i)
        if 'Quantitative Development/Quantitative Research' in j:
            seniorCentQ.append(i)

for i in seniorMountain:
    for j in i:
        if 'Data Science' in j:
            seniorMountData.append(i)
        if 'Product Management' in j:
            seniorMountPM.append(i)
        if 'Software Engineering' in j:
            seniorMountUI.append(i)
        if 'Quantitative Development/Quantitative Research' in j:
            seniorMountQ.append(i)

for i in seniorPacific:
    for j in i:
        if 'Data Science' in j:
            seniorPacData.append(i)
        if 'Product Management' in j:
            seniorPacPM.append(i)
        if 'Software Engineering' in j:
            seniorPacUI.append(i)
        if 'Quantitative Development/Quantitative Research' in j:
            seniorPacQ.append(i)

for i in juniorEastern:
    for j in i:
        if 'Data Science' in j:
            jEastData.append(i)
        if 'Product Management' in j:
            jEastPM.append(i)
        if 'Software Engineering' in j:
            jEastUI.append(i)
        if 'Quantitative Development/Quantitative Research' in j:
            jEastQ.append(i)

for i in juniorCentral:
    for j in i:
        if 'Data Science' in j:
            jCentData.append(i)
        if 'Product Management' in j:
            jCentPM.append(i)
        if 'Software Engineering' in j:
            jCentUI.append(i)
        if 'Quantitative Development/Quantitative Research' in j:
            jCentQ.append(i)

for i in juniorMountain:
    for j in i:
        if 'Data Science' in j:
            jMountData.append(i)
        if 'Product Management' in j:
            jMountPM.append(i)
        if 'Software Engineering' in j:
            jMountUI.append(i)
        if 'Quantitative Development/Quantitative Research' in j:
            jMountQ.append(i)

for i in juniorPacific:
    for j in i:
        if 'Data Science' in j:
            jPacData.append(i)
        if 'Product Management' in j:
            jPacPM.append(i)
        if 'Software Engineering' in j:
            jPacUI.append(i)
        if 'Quantitative Development/Quantitative Research' in j:
            jPacQ.append(i)


for i in sophEastern:
    for j in i:
        if 'Data Science' in j:
            soEastData.append(i)
        if 'Product Management' in j:
            soEastPM.append(i)
        if 'Software Engineering' in j:
            soEastUI.append(i)
        if 'Quantitative Development/Quantitative Research' in j:
            soEastQ.append(i)

for i in sophCentral:
    for j in i:
        if 'Data Science' in j:
            soCentData.append(i)
        if 'Product Management' in j:
            soCentPM.append(i)
        if 'Software Engineering' in j:
            soCentUI.append(i)
        if 'Quantitative Development/Quantitative Research' in j:
            soCentQ.append(i)

for i in sophMountain:
    for j in i:
        if 'Data Science' in j:
            soMountData.append(i)
        if 'Product Management' in j:
            soMountPM.append(i)
        if 'Software Engineering' in j:
            soMountUI.append(i)
        if 'Quantitative Development/Quantitative Research' in j:
            soMountQ.append(i)

for i in sophPacific:
    for j in i:
        if 'Data Science' in j:
            soPacData.append(i)
        if 'Product Management' in j:
            soPacPM.append(i)
        if 'Software Engineering' in j:
            soPacUI.append(i)
        if 'Quantitative Development/Quantitative Research' in j:
            soPacQ.append(i)


for i in freshEastern:
    for j in i:
        if 'Data Science' in j:
            frEastData.append(i)
        if 'Product Management' in j:
            frEastPM.append(i)
        if 'Software Engineering' in j:
            frEastUI.append(i)
        if 'Quantitative Development/Quantitative Research' in j:
            frEastQ.append(i)

for i in freshCentral:
    for j in i:
        if 'Data Science' in j:
            frCentData.append(i)
        if 'Product Management' in j:
            frCentPM.append(i)
        if 'Software Engineering' in j:
            frCentUI.append(i)
        if 'Quantitative Development/Quantitative Research' in j:
            frCentQ.append(i)

for i in freshMountain:
    for j in i:
        if 'Data Science' in j:
            frMountData.append(i)
        if 'Product Management' in j:
            frMountPM.append(i)
        if 'Software Engineering' in j:
            frMountUI.append(i)
        if 'Quantitative Development/Quantitative Research' in j:
            frMountQ.append(i)

for i in freshPacific:
    for j in i:
        if 'Data Science' in j:
            frPacData.append(i)
        if 'Product Management' in j:
            frPacPM.append(i)
        if 'Software Engineering' in j:
            frPacUI.append(i)
        if 'Quantitative Development/Quantitative Research' in j:
            frPacQ.append(i)



seData= list(zip(*(iter(seniorEastData),) * 3))
sePM = list(zip(*(iter(seniorEastPM),) * 3))
seSWE = list(zip(*(iter(seniorEastUI),) * 3))
seQ = list(zip(*(iter(seniorEastQ),) * 3))
scData= list(zip(*(iter(seniorCentData),) * 3))
scPM = list(zip(*(iter(seniorCentPM),) * 3))
scSWE = list(zip(*(iter(seniorCentUI),) * 3))
scQ = list(zip(*(iter(seniorCentQ),) * 3))
smData= list(zip(*(iter(seniorMountData),) * 3))
smPM = list(zip(*(iter(seniorMountPM),) * 3))
smSWE = list(zip(*(iter(seniorMountUI),) * 3))
smQ = list(zip(*(iter(seniorMountQ),) * 3))
spData= list(zip(*(iter(seniorPacData),) * 3))
spPM = list(zip(*(iter(seniorPacPM),) * 3))
spSWE = list(zip(*(iter(seniorPacUI),) * 3))
spQ = list(zip(*(iter(seniorPacQ),) * 3))

jeData= list(zip(*(iter(jEastData),) * 3))
jePM = list(zip(*(iter(jEastPM),) * 3))
jeSWE = list(zip(*(iter(jEastUI),) * 3))
jeQ = list(zip(*(iter(jEastQ),) * 3))
jcData= list(zip(*(iter(jCentData),) * 3))
jcPM = list(zip(*(iter(jCentPM),) * 3))
jcSWE = list(zip(*(iter(jCentUI),) * 3))
jcQ = list(zip(*(iter(jCentQ),) * 3))
jmData= list(zip(*(iter(jMountData),) * 3))
jmPM = list(zip(*(iter(jMountPM),) * 3))
jmSWE = list(zip(*(iter(jMountUI),) * 3))
jmQ = list(zip(*(iter(jMountQ),) * 3))
jpData= list(zip(*(iter(jPacData),) * 3))
jpPM = list(zip(*(iter(jPacPM),) * 3))
jpSWE = list(zip(*(iter(jPacUI),) * 3))
jpQ = list(zip(*(iter(jPacQ),) * 3))

soeData= list(zip(*(iter(soEastData),) * 3))
soePM = list(zip(*(iter(soEastPM),) * 3))
soeSWE = list(zip(*(iter(soEastUI),) * 3))
soeQ = list(zip(*(iter(soEastQ),) * 3))
socData= list(zip(*(iter(soCentData),) * 3))
jcPM = list(zip(*(iter(jCentPM),) * 3))
jcSWE = list(zip(*(iter(jCentUI),) * 3))
jcQ = list(zip(*(iter(jCentQ),) * 3))
jmData= list(zip(*(iter(jMountData),) * 3))
jmPM = list(zip(*(iter(jMountPM),) * 3))
jmSWE = list(zip(*(iter(jMountUI),) * 3))
jmQ = list(zip(*(iter(jMountQ),) * 3))
jpData= list(zip(*(iter(jPacData),) * 3))
jpPM = list(zip(*(iter(jPacPM),) * 3))
jpSWE = list(zip(*(iter(jPacUI),) * 3))
jpQ = list(zip(*(iter(jPacQ),) * 3))

seniorOfficialList = seData + sePM + seSWE + seQ + scData+scSWE+scPM+scQ+smData+smPM+smSWE+smQ+spData+spPM+spQ+spSWE
junOfficialList = jeData + jePM + jeSWE + jeQ + jcData+jcSWE+jcPM+scQ+jmData+jmPM+jmSWE+jmQ+jpData+jpPM+jpQ+jpSWE
sophOffcialList=soeData + soePM + soeSWE + soeQ + socData+socSWE+socPM+socQ+somData+somPM+smSWE+smQ+sopData+sopPM+spQ+sopSWE
freshOfficialList=feData + fePM + feSWE + feQ + fcData+fcSWE+fcPM+fcQ+fmData+fmPM+fmSWE+fmQ+fpData+fpPM+fpQ+fpSWE










