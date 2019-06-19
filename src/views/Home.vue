<template>
    <div class="home">
        <HomeHero></HomeHero>
        <About id="AboutSection"></About>
        <Skills id="SkillsSection"></Skills>
        <Timeline id="TimelineSection"></Timeline>
        <Contact id="ContactSection"></Contact>
    </div>
</template>

<script>
// @ is an alias to /src
import HomeHero from '@/components/HomeHero.vue';
import About from '@/components/About.vue';
import Skills from '@/components/Skills.vue';
import Timeline from '@/components/Timeline.vue';
import Contact from '@/components/Contact.vue';

export default {
    name: 'home',
    components: {
        HomeHero,
        About,
        Skills,
        Timeline,
        Contact
    }
};
</script>
