<template>
    <section class="section">
        <h3 class="subtitle is-3">
            A little about myself
        </h3>
        <div class="columns">
            <div class="column">
                my skills
            </div>
            <div class="column">
                my experience
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: 'About'
};
</script>

<style scoped>
.section {
    flex-direction: column;
    flex: 1;
}

h3 {
    margin-left: 5%;
}

</style>
