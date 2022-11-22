# Update your container registry name here
CONTINAER_REG="fancy.azurecr.io"
# Build Matchmaker image
cd Matchmaker/platform_scripts/bash
docker build -t matchmaker:4.27 -f Dockerfile ../..
# Build Signalling image
cd SignallingWebServer/platform_scripts/bash/
docker build -t signallingwebserver:4.27 -f ./Dockerfile ../..
# Build Unreal Engine App image . Copy the Dockerfile to the root of the Unreal Engine App
cd Game
docker build -t game:4.27 -f Dockerfile .
# Build TURN Server image
cd TURN
docker build -t turn -f Dockerfile .
# Build PlayerMonitor image
cd PlayerMonitor
docker build -t playermonitor -f Dockerfile .
# Build ScaleMonitor Image
cd ScaleMonitor
docker build -t scalemonitor -f Dockerfile .
# Tag and push images to container registry
docker tag matchmaker:4.27 $CONTINAER_REG/matchmaker:4.27
docker tag signallingwebserver:4.27 $CONTINAER_REG/signallingwebserver:4.27
docker tag game:4.27 $CONTINAER_REG/game:4.27
docker tag turn $CONTINAER_REG/turn
docker tag playermonitor $CONTINAER_REG/playermonitor
docker tag scalemonitor $CONTINAER_REG/scalemonitor
docker push $CONTINAER_REG/matchmaker:4.27
docker push $CONTINAER_REG/signallingwebserver:4.27
docker push $CONTINAER_REG/game:4.27
docker push $CONTINAER_REG/turn
docker push $CONTINAER_REG/playermonitor
docker push $CONTINAER_REG/scalemonitor

