<template>
    <section class="hero">
        <div class="container">
            <h1 class="title animated fadeInDown delay-1s" id="helloTitle">
                Hello there, I'm Matt!
            </h1>
            <h2 class="subtitle animated fadeIn delay-2s" id="introSubtitle">
                I'm a software engineer.
            </h2>
            <a href="#AboutSection" class="animated fadeInUp delay-3s">
                <span class="icon">
                    <i class="fas fa-angle-down" id="arrowIcon"></i>
                </span>
            </a>
        </div>
    </section>
</template>

<script>



export default {
    name: 'HomeHero',
    mounted() {
        var viewportWidth = window.innerWidth || document.documentElement.clientWidth;

        if (viewportWidth > 640) {
            document.getElementById('helloTitle').classList.add('is-1');
            document.getElementById('introSubtitle').classList.add('is-2');
            document.getElementById('arrowIcon').classList.add('fa-4x');
        } else {
            document.getElementById('helloTitle').classList.add('is-3');
            document.getElementById('introSubtitle').classList.add('is-4');
            document.getElementById('arrowIcon').classList.add('fa-2x');
        }
    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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
.icon {
    color: darkgrey;
    margin-top: 50%;
}
.hero {
    height: 100vh;
    background: url('../assets/mountain.jpeg');
    background-size: cover;
    /*
    width: 100%;
    height: 100%;
    max-height: 100%;
    */
}
@media screen and (max-width: 900px) and (orientation:portrait) {
    .hero {
        height: 100vh;
        background: url('../assets/mountaincropped.jpeg');
        background-size: cover;
    }
    .icon {
        margin-top: 130%;
    }
}
@media screen and (max-width: 700px) and (orientation:landscape) {
    .hero {
        height: 100vh;
        background: url('../assets/mountain.jpeg');
        background-size: cover;
    }
    .icon {
        margin-top: 25%;
    }
}
/**
  .hero {
    height: 100vh;
    background: url('http://source.unsplash.com/0BhSKStVtdM') no-repeat;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    border: 10px red dashed;
  }
  */
</style>
