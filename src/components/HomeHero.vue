<template>
    <section class="hero">
        <div class="container">
            <h1 class="title is-1 animated fadeInDown delay-1s">
                Hello there, I'm Matt!
            </h1>
            <h2 class="subtitle is-2 animated fadeIn delay-2s">
                I'm a software engineer.
            </h2>
            <a href="#AboutSection" class="animated fadeInUp delay-3s">
                <span class="icon">
                    <i class="fas fa-angle-down fa-4x"></i>
                </span>
            </a>
        </div>
    </section>
</template>

<script>
export default {
    name: 'HomeHero',
    props: {
        msg: String
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
    background: url('http://source.unsplash.com/ddLiNMqWAOM');
    background-size: cover;
    /*
    width: 100%;
    height: 100%;
    max-height: 100%;
    */
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
