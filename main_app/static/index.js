let quoteArr =['you better get better quotes','dont count your eggs too soon','okie dokie smokie','bye','good luck','sionara', 'babyboomers','tomorrow is a better day', 'dont rain on my prade']

console.log(quoteArr)

Promise.all([
  loadAsync(
    'https://res.cloudinary.com/dbux8pdyi/video/upload/v1617739205/8_uqve8h_jwwgba.mp4'
  ),
  loadAsync(
    'https://res.cloudinary.com/dbux8pdyi/video/upload/v1617739205/9_h3zaob_e6dnwa.mp4'
  ),
  loadAsync(
    'https://res.cloudinary.com/dbux8pdyi/video/upload/v1617739210/11_cr2uom_gv8fv9.mp4'
  ),
  loadAsync(
    'https://res.cloudinary.com/dbux8pdyi/video/upload/v1617739204/12q_i8przi_qawjjt.mp4'
  ),
  loadAsync(
    'https://res.cloudinary.com/dbux8pdyi/video/upload/v1617739199/13_kpzt8r_mrzw9i.mp4'
  ),
  loadAsync(
    'https://res.cloudinary.com/dbux8pdyi/video/upload/v1617739197/4_nqdsdn_boenrw.mp4'
  ),
  loadAsync(
    'https://res.cloudinary.com/dbux8pdyi/video/upload/v1617739195/5_xhz9of_fgsu7l.mp4'
  ),
  loadAsync(
    'https://res.cloudinary.com/dbux8pdyi/video/upload/v1617739197/6_v9cxwu_w3vtwk.mp4'
  ),
]).then(result => {
        webgl.texturesArray = result;
        document.getElementById("wrapper").addEventListener("click", changeTexture, false);
    });

    <script>
function ReLoadImages(){
    $('img[data-lazysrc]').each( function(){
        //* set the img src from data-src
        $( this ).attr( 'src', $( this ).attr( 'data-lazysrc' ) );
        }
    );
}

document.addEventListener('readystatechange', event => {
    if (event.target.readyState === "interactive") {  //or at "complete" if you want it to execute in the most last state of window.
        ReLoadImages();
    }
});
</script>
