<template>
    <div class="home">
        <HomeHero></HomeHero>
        <About id="AboutSection"></About>
        <Skills id="SkillsSection"></Skills>
        <Timeline id="TimelineSection"></Timeline>
    </div>
</template>

<script>
// @ is an alias to /src
import HomeHero from '@/components/HomeHero.vue';
import About from '@/components/About.vue';
import Skills from '@/components/Skills.vue';
import Timeline from '@/components/Timeline.vue';

export default {
    name: 'home',
    components: {
        HomeHero,
        About,
        Skills,
        Timeline
    }
};
</script>
