az aks nodepool add \
    --resource-group pixel_group \
    --cluster-name pix \
    --name gpunp \
    --node-count 1 \
    --node-vm-size Standard_NC12_Promo \
    --node-taints sku=gpu:NoSchedule \
    --aks-custom-headers UseGPUDedicatedVHD=true \
    --node-osdisk-size 250 \
    --mode User 
    

az aks nodepool add \
    --resource-group pixel_group \
    --cluster-name pix \
    --name turnp \
    --node-count 1 \
    --node-vm-size Standard_F8s_v2 \
    --node-taints sku=turn:NoSchedule \
    --node-osdisk-size 250 \
    --mode User \
    --enable-node-public-ip



