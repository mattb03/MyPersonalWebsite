<template>
    <section class="hero" id="sectionHero">
        <div class="container">
            <h1 class="title animated fadeInDown delay-1s" id="helloTitle">
                Hello there, I'm Matt!
            </h1>
            <h2 class="subtitle animated fadeIn delay-2s" id="introSubtitle">
                I'm a software engineer.
            </h2>
            <a href="#AboutSection"> <!-- TODO: give this <a> an id, use it for margin-top instead of <i> element -->
                <span class="icon">
                    <i class="fas fa-angle-down animated fadeInUp delay-3s" id="arrowIcon"></i>
                </span>
            </a>
        </div>
    </section>
</template>

<script>



export default {
    name: 'HomeHero',
    methods: {
        handleResize: function() {
            var viewportWidth = window.innerWidth || document.documentElement.clientWidth;
            //var orientation = screen.msOrientation || screen.mozOrientation || (screen.orientation || {}).type;
            // need to finish this function, copy and use the conditions from mounted()
        }
    },
    mounted() {
        var viewportWidth = window.innerWidth || document.documentElement.clientWidth;
        var orientation = screen.msOrientation || screen.mozOrientation || (screen.orientation || {}).type;
        if (viewportWidth > 800) {
                document.getElementById('helloTitle').classList.add('is-1');
                document.getElementById('introSubtitle').classList.add('is-2');
                document.getElementById('arrowIcon').classList.add('fa-4x');
            if (orientation === 'landscape-primary' || orientation === 'landscape-secondary') {
                document.getElementById('arrowIcon').classList.add('icon-default');
                document.getElementById('sectionHero').classList.add('hero-large');
            } else {
                document.getElementById('arrowIcon').classList.add('icon-portrait-small');
                document.getElementById('sectionHero').classList.add('hero-portrait-small');
            }

        } else {
            document.getElementById('helloTitle').classList.add('is-3');
            document.getElementById('introSubtitle').classList.add('is-4');
            document.getElementById('arrowIcon').classList.add('fa-2x');
            document.getElementById('arrowIcon').classList.add('icon-portrait-small');
            document.getElementById('sectionHero').classList.add('hero-portrait-small');
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
@media screen and (max-width: 900px) and (orientation:portrait) {
    .hero-portrait-small {
        height: 100vh;
        background: url('../assets/mountaincropped.jpeg');
        background-size: cover;
    }
    .icon-portrait-small {
        color: darkgrey;
        margin-top: 130%;
    }
}
@media screen and (max-width: 700px) and (orientation:landscape) {
    .icon-landscape-small {
        color: darkgrey;
        margin-top: 25%;
    }
}
</style>
