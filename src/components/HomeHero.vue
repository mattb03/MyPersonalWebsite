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
            var viewportHeight = window.innerHeight;

            if (viewportWidth < 450 && viewportHeight < 850) {

                // mobile portrait
                document.getElementById('helloTitle').classList.add('is-3');
                document.getElementById('introSubtitle').classList.add('is-4');
                document.getElementById('arrowIcon').classList.add('fa-2x');
            } else if (viewportWidth < 850 && viewportHeight < 450) {

                // mobile landscape
                document.getElementById('helloTitle').classList.add('is-3');
                document.getElementById('introSubtitle').classList.add('is-4');
                document.getElementById('arrowIcon').classList.add('fa-2x');
            } else if (viewportWidth < 900 && viewportHeight > 1000) {

                // tablet portrait
                document.getElementById('helloTitle').classList.add('is-1');
                document.getElementById('introSubtitle').classList.add('is-2');
                document.getElementById('arrowIcon').classList.add('fa-4x');
            } else if (viewportWidth > 1000 && viewportHeight < 900) {

                // tablet landscape
                document.getElementById('helloTitle').classList.add('is-1');
                document.getElementById('introSubtitle').classList.add('is-2');
                document.getElementById('arrowIcon').classList.add('fa-4x');
            } else {
                document.getElementById('helloTitle').classList.remove('is-3');
                document.getElementById('introSubtitle').classList.remove('is-4');

                // desktop
                document.getElementById('helloTitle').classList.add('is-1');
                document.getElementById('introSubtitle').classList.add('is-2');
                document.getElementById('arrowIcon').classList.add('fa-4x');
            }
        },

    },
    mounted() {
        var viewportWidth = window.innerWidth || document.documentElement.clientWidth;
        var viewportHeight = window.innerHeight;

        document.getElementById('sectionHero').classList.add('hero-large');
        if (viewportWidth < 450 && viewportHeight < 850) {
            // mobile portrait
            document.getElementById('helloTitle').classList.add('is-3');
            document.getElementById('introSubtitle').classList.add('is-4');
            document.getElementById('arrowIcon').classList.add('fa-2x');
        } else if (viewportWidth < 850 && viewportHeight < 450) {
            // mobile landscape
            document.getElementById('helloTitle').classList.add('is-3');
            document.getElementById('introSubtitle').classList.add('is-4');
            document.getElementById('arrowIcon').classList.add('fa-2x');
        } else if (viewportWidth < 900 && viewportHeight > 1000) {
            // tablet portrait
            document.getElementById('helloTitle').classList.add('is-1');
            document.getElementById('introSubtitle').classList.add('is-2');
            document.getElementById('arrowIcon').classList.add('fa-4x');
        } else if (viewportWidth > 1000 && viewportHeight < 900) {
            // tablet landscape
            document.getElementById('helloTitle').classList.add('is-1');
            document.getElementById('introSubtitle').classList.add('is-2');
            document.getElementById('arrowIcon').classList.add('fa-4x');
        } else {
            // desktop
            document.getElementById('helloTitle').classList.add('is-1');
            document.getElementById('introSubtitle').classList.add('is-2');
            document.getElementById('arrowIcon').classList.add('fa-4x');
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
a {
    color: darkgrey;
}
.container {
    margin: 5% 30% 30% 30%;
    flex-direction: column;
}
.title,
.subtitle {
    color: darkgrey;
}

.hero-large {
    height: 100vh;
    background: url('../assets/mountain.jpeg');
    background-size: cover;
    background-position: center;

}
.hero-small {
    height: 100vh;
    background: url('../assets/mountaincropped.jpeg');
    background-size: cover;
}

#arrowIcon {
    position: absolute;
    top: 70vh;
    padding: 20px;
}


</style>
