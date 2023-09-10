#!/bin/bash

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
TODAY=$(date)
NEGATIVE=$(echo $DATA | jq '.[0].negative')
DEATH=$(echo $DATA | jq '.[0].death')
HOSPITAL=$(echo $DATA | jq '.[0].hospitalizedCumulative')
STATES=$(echo $DATA | jq '.[0].states')
PENDING=$(echo $DATA | jq '.[0].pending')
TESTRESULTS=$(echo $DATA | jq '.[0].totalTestResults')


echo "On $TODAY, there were $POSITIVE positive COVID cases, $NEGATIVE negative tests, $DEATH deaths and $HOSPITAL hospitalized.  These COVID tests span over $STATES states, with $PENDING pending cases still out there.  On this current date, there have been a total of $TESTRESULTS COVID tests taken."
