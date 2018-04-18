#!/bin/bash

THIS_DIR=$(cd ${0%/*} && echo $PWD)
APP_BIN_DIR=$THIS_DIR/../bin

bootstrap() {

export WAIFU2X_INPUT_IMAGE=./assets/pics/render-480.jpg
export WAIFU2X_OUTPUT_IMAGE=./assets/pics/render.result.jpg
export WAIFU2X_MODEL_DIR=./assets/models/vgg_7/photo

}

run() {
    # reset
cargo run --release -- -i $WAIFU2X_INPUT_IMAGE -o $WAIFU2X_OUTPUT_IMAGE -m noise_scale   -s 2 -d $WAIFU2X_MODEL_DIR
}


main() {

    bootstrap
    run
}

main

