<template>
  <section class="w-full py-6 md:py-12 lg:py-16">
    <div class="container px-4 md:px-6">
      <div class="grid items-center gap-6 lg:grid-cols-2 lg:gap-12">
        <div class="space-y-4">
          <h2 class="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">
            Discover. Share. Engage.
          </h2>
          <p class="max-w-[700px] text-gray-500 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed dark:text-gray-400">
            Content Hub is your gateway to a world of captivating stories,
            inspiring articles, and thought-provoking essays. Discover new
            perspectives, share your favorite content with the world, and
            engage with a vibrant community of readers and creators.
          </p>
        </div>
        <div class="grid items-start gap-4">
          <div class="grid items-center gap-2">
            <!-- <img
              alt="Discover"
              class="rounded-lg object-cover w-16 h-16"
              height="100"
              src="/placeholder.svg"
              style="aspect-ratio: 100/100; object-fit: cover;"
              width="100"
            /> -->
            <div class="grid items-start gap-1">
              <h3 class="font-bold">Discover</h3>
              <p class="text-sm text-gray-500 dark:text-gray-400">
                Explore new and exciting content across different
                categories.
              </p>
            </div>
          </div>
          <div class="grid items-center gap-2">
            <!-- <img
              alt="Share"
              class="rounded-lg object-cover w-16 h-16"
              height="100"
              src="/placeholder.svg"
              style="aspect-ratio: 100/100; object-fit: cover;"
              width="100"
            /> -->
            <div class="grid items-start gap-1">
              <h3 class="font-bold">Share</h3>
              <p class="text-sm text-gray-500 dark:text-gray-400">
                Easily share your favorite articles, stories, and more with
                others.
              </p>
            </div>
          </div>
          <div class="grid items-center gap-2">
            <!-- <img
              alt="Engage"
              class="rounded-lg object-cover w-16 h-16"
              height="100"
              src="/placeholder.svg"
              style="aspect-ratio: 100/100; object-fit: cover;"
              width="100"
            /> -->
            <div class="grid items-start gap-1">
              <h3 class="font-bold">Engage</h3>
              <p class="text-sm text-gray-500 dark:text-gray-400">
                Connect with other readers and creators, join discussions,
                and more.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "component",
  functional: true,
};
</script>

<style scoped>
.section {
  background-color: #f9fafb;
}

</style>

