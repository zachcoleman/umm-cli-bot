docker build . -t umm-server

docker run \
    -v /Users/zachcoleman/umm-cli-helper/umm/resources/:/root/.umm \
    -p 7026:7026 \
    umm-server