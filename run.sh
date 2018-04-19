#!/bin/bash

THIS_DIR=$(cd ${0%/*} && echo $PWD)

bootstrap() {

    export PATH=$THIS_DIR/target/release:$PATH
    export WAIFU2X_MODEL_DIR=${THIS_DIR}/assets/models/vgg_7/photo

    # build waifu2x
    cargo build --release
}

run_test_case() {

    local test_case_name=$1
    local input_image_small=${THIS_DIR}/assets/pics/${test_case_name}/render-480.jpg
    local input_image_large=${THIS_DIR}/assets/pics/${test_case_name}/render-960.jpg

    local target_image_small=${THIS_DIR}/target/${test_case_name}/render-small.jpg
    local target_image_large=${THIS_DIR}/target/${test_case_name}/render.jpg

    local target_image_gm=${THIS_DIR}/target/${test_case_name}/render.gm.jpg
    local target_image_n1=${THIS_DIR}/target/${test_case_name}/render.n1.jpg
    local target_image_n2=${THIS_DIR}/target/${test_case_name}/render.n2.jpg

    rm -rf ${THIS_DIR}/target/${test_case_name}
    mkdir -p ${THIS_DIR}/target/${test_case_name}

    echo "testcase: ${test_case_name}"

    echo "  copy file to target"
    cp -f $input_image_small $target_image_small
    cp -f $input_image_large $target_image_large

    echo "  scale 2x by graphicsmagick"
    gm convert $target_image_small -resize 960x540 $target_image_gm

    echo "  scale 2x by waifu2x"
    waifu2x-hsa -i $target_image_small -o $target_image_n1 -m noise_scale -n 1  -s 2 -d $WAIFU2X_MODEL_DIR

    echo "  scale 2x and denoise by waifu2x"
    waifu2x-hsa -i $target_image_small -o $target_image_n2 -m noise_scale -n 2  -s 2 -d $WAIFU2X_MODEL_DIR

}

run_test_cases() {

    run_test_case livingroom
    run_test_case bookshelf
}


main() {
    bootstrap
    run_test_cases
}

main

