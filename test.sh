source .env
for ((i = 0; i < ${#ExtendConfig[*]}; i++)); do
  svrconf=${ExtendConfig[i]}
  yq e ".proxies" ./conf/config.yaml

  #yq e '.proxies += ["'$svrconf'"]' conf/config.yaml >test.yaml
done
