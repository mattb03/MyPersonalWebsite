<template>
    <section class="section">
        <div class="container" style="max-width: 50vw;">
            <h3 class="subtitle is-3">Contact Me</h3>
            <!-- TODO: figure out how to align the name and email boxes with the message box -->
            <div class="columns">
                <div class="field column">
                    <label class="label">Name</label>
                    <div class="control">
                        <input type="text" class="input" placeholder="Enter name">
                    </div>
                </div>
                <div class="field column">
                    <label class="label">Email</label>
                    <div class="control">
                        <input type="text" class="input" placeholder="Enter email">
                    </div>
                </div>
            </div>
            <div class="field column">
                <label class="label">Message</label>
                <div class="control">
                    <textarea cols="30" rows="10" class="textarea">Enter a message</textarea>
                </div>
            </div>
            <div class="field">
                <div class="control">
                    <button class="button is-link">Submit</button>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: 'Contact'
};
</script>

<style scoped>
button {
    /* TODO: figure out how to center the submit button */
}
</style>

