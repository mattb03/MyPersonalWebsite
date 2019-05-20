<template>
    <div class="home">
        <HomeHero></HomeHero>
        <About></About>
    </div>
</template>

<script>
// @ is an alias to /src
import HomeHero from '@/components/HomeHero.vue';
import About from '@/components/About.vue';

export default {
    name: 'home',
    components: {
        HomeHero,
        About
    }
};
</script>
