# Update your container registry name here
CONTINAER_REG="fancy.azurecr.io"
# Build Matchmaker image
cd Matchmaker/platform_scripts/bash
docker build -t matchmaker:4.27 -f Dockerfile ../..
# Build Signalling image
cd SignallingWebServer/platform_scripts/bash/
docker build -t signallingwebserver:4.27 -f ./Dockerfile ../..
# Build Unreal Engine App image . Copy the Dockerfile to the root of the Unreal Engine App
cd Game/Dockerfile
docker build -t game:4.27 -f Dockerfile .
# Tag and push images to container registry
docker tag matchmaker:4.27 $CONTINAER_REG/matchmaker:4.27
docker tag signallingwebserver:4.27 $CONTINAER_REG/signallingwebserver:4.27
docker tag game:4.27 $CONTINAER_REG/game:4.27
docker push $CONTINAER_REG/matchmaker:4.27
docker push $CONTINAER_REG/signallingwebserver:4.27
docker push $CONTINAER_REG/game:4.27
