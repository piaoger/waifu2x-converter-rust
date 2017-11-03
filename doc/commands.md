commands.md


export ROOT_DIR=~/workspace

export WAIFU2X_INPUT_IMAGE=$ROOT_DIR/cae80c57826c4a79aad829b74d076a9f-rs.jpg
export WAIFU2X_OUTPUT_IMAGE=$ROOT_DIR/cae80c57826c4a79aad829b74d076a9f-o.jpg
export WAIFU2X_MODEL_DIR=$ROOT_DIR/waifu2x/models/photo
date
./target/release/waifu2x-hsa -i $WAIFU2X_INPUT_IMAGE -o $WAIFU2X_OUTPUT_IMAGE -m noise_scale  -n 2    -d $WAIFU2X_MODEL_DIR
date
date



export WAIFU2X_INPUT_IMAGE=~/workspace/repository/machine.learning/fix/testcases_origin-adjustment-shadow/case-1/1-origin.jpg
export WAIFU2X_OUTPUT_IMAGE=~/workspace/repository/machine.learning/fix/testcases_origin-adjustment-shadow/case-1/output.png
export WAIFU2X_MODEL_DIR=/~/w/dev/rust/waifu2x/models/photo


export WAIFU2X_INPUT_IMAGE=~/workspace/repository/machine.learning/vrscenescene-1024x1024.jpeg
export WAIFU2X_OUTPUT_IMAGE=~/workspace/repository/machine.learning/vrscenescene-2048x2048.jpeg
export WAIFU2X_MODEL_DIR=/~/w/dev/rust/waifu2x/models/photo


cargo run --release -- -i $WAIFU2X_INPUT_IMAGE -o $WAIFU2X_OUTPUT_IMAGE -m noise_scale  -n 2  -s 2 -d $WAIFU2X_MODEL_DIR


export WAIFU2X_INPUT_IMAGE=~/workspace/repository/machine.learning/12950290_1004276509662437_788923829_n.jpg
export WAIFU2X_OUTPUT_IMAGE=~/workspace/repository/machine.learning/12950290_1004276509662437_788923829_n-o.jpg
export WAIFU2X_MODEL_DIR=/~/w/dev/rust/waifu2x/models/anime_style_art_rgb
cargo run --release -- -i $WAIFU2X_INPUT_IMAGE -o $WAIFU2X_OUTPUT_IMAGE -m noise_scale  -n 2  -s 2 -d $WAIFU2X_MODEL_DIR



export WAIFU2X_INPUT_IMAGE=~/workspace/repository/machine.learning/input3.png
export WAIFU2X_OUTPUT_IMAGE=~/workspace/repository/machine.learning/input3-o.png
export WAIFU2X_MODEL_DIR=/~/w/dev/rust/waifu2x/models/anime_style_art_rgb
cargo run --release -- -i $WAIFU2X_INPUT_IMAGE -o $WAIFU2X_OUTPUT_IMAGE -m noise_scale  -n 2  -s 2 -d $WAIFU2X_MODEL_DIR


export WAIFU2X_INPUT_IMAGE=~/Downloads/origin.jpeg
export WAIFU2X_OUTPUT_IMAGE=~/Downloads/after-o.jpeg
export WAIFU2X_MODEL_DIR=/~/w/dev/rust/waifu2x/models/anime_style_art_rgb
cargo run --release -- -i $WAIFU2X_INPUT_IMAGE -o $WAIFU2X_OUTPUT_IMAGE -m noise_scale  -n 2  -s 2 -d $WAIFU2X_MODEL_DIR

