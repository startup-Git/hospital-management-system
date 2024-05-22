$('#carousel__sliders_owl').owlCarousel({
    items:1,
    loop:true,
    autoplay:true,
    autoplayTimeout:4000,
    autoplayHoverPause:false,
    animateOut: 'fadeOut',
    // animateIn: 'flipInX',
    smartSpeed:450,
    nav:false,
    dots: false,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:1
        },
        1000:{
            items:1
        }
    }
});

$('#specialist').owlCarousel({
    items:1,
    loop:true,
    margin:30,
    autoplay:true,
    autoplayTimeout:2000,
    autoplayHoverPause:true,
    animateOut: 'fadeOut',
    animateIn: 'flipInX',

    /*
    
    animateOut: 'fadeOut',
    stagePadding:30,
    smartSpeed:450,*/
    nav:true,
    dots: false,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:2
        },
        1000:{
            items:4
        }
    }
});


$('#testimonial_slide').owlCarousel({
    items:1,
    loop:true,
    margin:30,
    autoplay:true,
    autoplayTimeout:5000,
    autoplayHoverPause:true,
    nav:true,
    dots: false,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:1
        },
        1000:{
            items:1
        }
    }
})

$('#doctor_client').owlCarousel({
    loop:true,
    margin:10,
    margin:30,
    autoplay:true,
    autoplayTimeout:5000,
    autoplayHoverPause:true,
    nav:true,
    dots:false,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:1
        },
        1000:{
            items:1
        }
    }
})