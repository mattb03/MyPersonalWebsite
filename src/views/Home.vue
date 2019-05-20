<template>
    <div class="home">
        <HomeHero></HomeHero>
        <About id="AboutSection"></About>
        <Skills id="SkillsSection"></Skills>
    </div>
</template>

<script>
// @ is an alias to /src
import HomeHero from '@/components/HomeHero.vue';
import About from '@/components/About.vue';
import Skills from '@/components/Skills.vue';

export default {
    name: 'home',
    components: {
        HomeHero,
        About,
        Skills
    }
};
</script>
