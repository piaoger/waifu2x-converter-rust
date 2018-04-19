#!/bin/bash

THIS_DIR=$(cd ${0%/*} && echo $PWD)
APP_BIN_DIR=$THIS_DIR/../bin

bootstrap() {

    export WAIFU2X_INPUT_IMAGE=./assets/pics/render-480.jpg

    export WAIFU2X_TARGT_IMAGE_SMALL=./target/render-small.jpg
    export WAIFU2X_TARGT_IMAGE_RENDER=./target/render.jpg

    export WAIFU2X_TARGT_IMAGE_GM=./target/render.gm.jpg
    export WAIFU2X_TARGT_IMAGE_N1=./target/render.n1.jpg
    export WAIFU2X_TARGT_IMAGE_N2=./target/render.n2.jpg

    export PATH=$THIS_DIR/target/release:$PATH
    export WAIFU2X_MODEL_DIR=./assets/models/vgg_7/photo
}

run() {
    cargo build --release

    echo "copy file to target"
    cp -f $WAIFU2X_INPUT_IMAGE $WAIFU2X_TARGT_IMAGE_SMALL
    cp -f $WAIFU2X_INPUT_IMAGE $WAIFU2X_TARGT_IMAGE_RENDER

    echo "scale 2x by graphicsmagick"
    gm convert $WAIFU2X_TARGT_IMAGE_SMALL -resize 960x540 $WAIFU2X_TARGT_IMAGE_GM

    echo "scale 2x by waifu2x"
    waifu2x-hsa -i $WAIFU2X_TARGT_IMAGE_SMALL -o $WAIFU2X_TARGT_IMAGE_N1 -m noise_scale -n 1  -s 2 -d $WAIFU2X_MODEL_DIR

    echo "scale 2x and denoise by waifu2x"
    waifu2x-hsa -i $WAIFU2X_TARGT_IMAGE_SMALL -o $WAIFU2X_TARGT_IMAGE_N2 -m noise_scale -n 2  -s 2 -d $WAIFU2X_MODEL_DIR
}


main() {
    bootstrap
    run
}

main

