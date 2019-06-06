<template>
    <section class="hero" id="sectionHero">
        <div class="container">
            <h1 class="title animated fadeInDown delay-1s" id="helloTitle">
                Hello there, I'm Matt!
            </h1>
            <h2 class="subtitle animated fadeIn delay-2s" id="introSubtitle">
                I'm a software engineer.
            </h2>
            <a href="#AboutSection" id="arrowHref"> <!-- TODO: give this <a> an id, use it for margin-top instead of <i> element -->
                <span class="icon" id="arrowIcon">
                    <i class="fas fa-angle-down animated fadeInUp delay-3s"></i>
                </span>
            </a>
        </div>
    </section>
</template>

<script>



export default {
    name: 'HomeHero',
    data: function() {
        return {
            viewportWidth: window.innerWidth || document.documentElement.clientWidth,
            orientation: screen.msOrientation || screen.mozOrientation || (screen.orientation || {}).type
        }
    },
    methods: {
        handleResize: function() {
            var viewportWidth = window.innerWidth || document.documentElement.clientWidth;
            if (viewportWidth > 900) {
                // desktop
                this.resizeDesktop();
            } else {
                if (viewportWidth > 700) {
                    // ipad/tablet portrait
                    this.resizeTablet();
                } else {
                    // mobile 
                    this.resizeMobile();
                }
            }
        },
        resizeMobile: function() {
                var viewportWidth = window.innerWidth || document.documentElement.clientWidth;
                document.getElementById('helloTitle').classList.remove('is-1');
                document.getElementById('introSubtitle').classList.remove('is-2');
                document.getElementById('arrowIcon').classList.remove('fa-4x');


                document.getElementById('helloTitle').classList.add('is-3');
                document.getElementById('introSubtitle').classList.add('is-4');
                document.getElementById('arrowIcon').classList.add('fa-2x');

                if (viewportWidth < 400) {
                    document.getElementById('arrowIcon').classList.remove('icon-landscape-small');
                    document.getElementById('arrowIcon').classList.add('icon-portrait-small');

                    document.getElementById('sectionHero').classList.remove('hero-large');
                    document.getElementById('sectionHero').classList.add('hero-small');
                } else {
                    document.getElementById('arrowIcon').classList.remove('icon-portrait-small');
                    document.getElementById('arrowIcon').classList.add('icon-landscape-small');

                    document.getElementById('sectionHero').classList.remove('hero-small');
                    document.getElementById('sectionHero').classList.add('hero-large');
                    
                }
        },
        resizeTablet: function() {
                document.getElementById('helloTitle').classList.remove('is-3');
                document.getElementById('introSubtitle').classList.remove('is-4');
                document.getElementById('arrowIcon').classList.remove('fa-2x');


                document.getElementById('helloTitle').classList.add('is-1');
                document.getElementById('introSubtitle').classList.add('is-2');
                document.getElementById('arrowIcon').classList.add('fa-4x');

                document.getElementById('arrowIcon').classList.remove('icon-portrait-small');
                document.getElementById('arrowIcon').classList.remove('icon-landscape-small');
                document.getElementById('arrowIcon').classList.add('icon-default');
                document.getElementById('sectionHero').classList.remove('hero-large');
                document.getElementById('sectionHero').classList.remove('hero-small'); // remove potential extra hero-small
                document.getElementById('sectionHero').classList.add('hero-small');
        },
        resizeDesktop: function() {
                document.getElementById('helloTitle').classList.remove('is-3');
                document.getElementById('introSubtitle').classList.remove('is-4');
                document.getElementById('arrowIcon').classList.remove('fa-2x');
                document.getElementById('arrowIcon').classList.remove('icon-portrait-small');
                document.getElementById('arrowIcon').classList.remove('icon-landscape-small');
                document.getElementById('sectionHero').classList.remove('hero-small');

                document.getElementById('helloTitle').classList.add('is-1');
                document.getElementById('introSubtitle').classList.add('is-2');
                document.getElementById('arrowIcon').classList.add('fa-4x');
                document.getElementById('arrowIcon').classList.add('icon-default');
                document.getElementById('sectionHero').classList.add('hero-large');
        }
    },
    mounted() {
        var viewportWidth = window.innerWidth || document.documentElement.clientWidth;
        if (viewportWidth > 900) {
            document.getElementById('helloTitle').classList.add('is-1');
            document.getElementById('introSubtitle').classList.add('is-2');
            document.getElementById('arrowIcon').classList.add('fa-4x');
            document.getElementById('arrowIcon').classList.add('icon-default');
            document.getElementById('sectionHero').classList.add('hero-large');
        } else {
            // small screen
            if (viewportWidth > 700) {
                // ipad/tablet portrait
                document.getElementById('helloTitle').classList.add('is-1');
                document.getElementById('introSubtitle').classList.add('is-2');
                document.getElementById('arrowIcon').classList.add('fa-4x');
                document.getElementById('arrowIcon').classList.add('icon-default');
                document.getElementById('sectionHero').classList.add('hero-small');
            } else {
                // mobile potrait/landscape
                document.getElementById('helloTitle').classList.add('is-3');
                document.getElementById('introSubtitle').classList.add('is-4');
                document.getElementById('arrowIcon').classList.add('fa-2x');

                if (viewportWidth < 400) {
                    document.getElementById('arrowIcon').classList.add('icon-portrait-small');
                    document.getElementById('sectionHero').classList.add('hero-small');
                } else {
                    document.getElementById('arrowIcon').classList.add('icon-landscape-small');
                    document.getElementById('sectionHero').classList.add('hero-large');
                }            
            }
        }
        window.addEventListener('resize', this.handleResize);
    }
};
</script>

<style scoped>
/*
  image1: rtCujH697DU
  image2: ddLiNMqWAOM
  image3: KidY3t8O4PE
*/

.container {
    margin: 15% 30% 30% 30%;
    flex-direction: column;
}
.title,
.subtitle {
    color: darkgrey;
}
.icon-default {
    color: darkgrey;
    margin-top: 50%;
}
.hero-large {
    height: 100vh;
    background: url('../assets/mountain.jpeg');
    background-size: cover;
}
.hero-small {
    height: 100vh;
    background: url('../assets/mountaincropped.jpeg');
    background-size: cover;
}
.icon-portrait-small {
    color: darkgrey;
    margin-top: 130%;
}
.icon-landscape-small {
    color: darkgrey;
    margin-top: 25%;
}
</style>
