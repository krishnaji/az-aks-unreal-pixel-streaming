FROM --platform=${BUILDPLATFORM:-linux/amd64} ghcr.io/epicgames/unreal-engine:dev-4.27 AS build

COPY --chown=ue4:ue4 . /project

WORKDIR  /project

RUN /home/ue4/UnrealEngine/Engine/Build/BatchFiles/RunUAT.sh \
    BuildCookRun \
    -utf8output \
    -platform=Linux \
    -clientconfig=Shipping \
    -serverconfig=Shipping \
    -project=/project/MyDemoProject.uproject \
    -noP4 -nodebuginfo -allmaps \
    -cook -build -stage -prereqs -pak -archive \
    -archivedirectory=/project/Packaged 

FROM --platform=${BUILDPLATFORM:-linux/amd64} ghcr.io/epicgames/unreal-engine:runtime-pixel-streaming
WORKDIR /home/ue4/project
COPY --from=build --chown=ue4:ue4 /project/Packaged/LinuxNoEditor ./

# More Configs: https://docs.unrealengine.com/4.27/en-US/SharingAndReleasing/PixelStreaming/PixelStreamingReference/
CMD ["/bin/bash", "-c", "./MyDemoProject.sh -PixelStreamingURL=${SIGNALSERVER_URL} -RenderOffscreen -Unattended -ResX=1920 -ResY=1080 -Windowed -ForceRes -StdOut" ]
