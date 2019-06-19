<template>
    <section class="section hero">
        <div class="container">
            <h3 class="subtitle is-3">Contact Me</h3>
            <!-- TODO: figure out how to align the name and email boxes with the message box -->
            <div class="columns is-centered">
                <div class="column">
                    <div class="field">
                        <label class="label">Name</label>
                        <div class="control">
                            <input type="text" class="input" placeholder="Enter name">
                        </div>
                    </div>
                </div>
                <div class="column">
                    <div class="field">
                        <label class="label">Email</label>
                        <div class="control">
                            <input type="text" class="input" placeholder="Enter email">
                        </div>
                    </div>
                </div>
            </div>
            <div class="columns is-centered">
                <div class="column">
                    <div class="field">
                        <label class="label">Message</label>
                        <div class="control">
                            <textarea cols="30" rows="10" class="textarea">Enter a message</textarea>
                        </div>
                    </div>
                </div>
            </div>
            <div class="columns is-centered">
                <div class="column is-one-third">
                    <div class="field">
                        <div class="control">
                            <button class="button is-rounded" type="submit">Submit</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: 'Contact',
    methods: {

    },
    mounted() {
    }
};
</script>

<style scoped>
@media only screen and (max-width: 769px) {
    button {
        margin-left: 38%;
    }
}
</style>

