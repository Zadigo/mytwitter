<template>
  <article class="card shadow-none border-light rounded-0 p-4 placeholder-glow" aria-hidden="true">
    <div class="card-header d-flex justify-content-between align-items-center border-0">
      <div class="d-flex justify-content-left align-items-center gap-4">
        <img :src="'...'" class="img-fluid rounded-circle placeholder" alt="...">
        <a class="disabled text-light">
          <span class="placeholder col-3"></span>
          <span class="placeholder col-3"></span>
        </a>
      </div>
      
      <button type="button" class="btn btn-light btn-floating disabled placeholder"></button>
    </div>

    <a class="disabled text-light">
      <div class="card-body px-5">
        <p>
          <span class="placeholder col-12"></span>
          <span class="placeholder col-6"></span>
          <span class="placeholder col-8"></span>
        </p>
      </div>
    </a>

    <div class="card-footer d-flex justify-content-around border-0 px-1">
      <button type="button" class="btn btn-light btn-rounded disabled placeholder"></button>
      <button type="button" class="btn btn-light btn-rounded disabled placeholder"></button>
      <button type="button" class="btn btn-light btn-rounded disabled placeholder"></button>
      <button type="button" class="btn btn-light btn-rounded disabled placeholder"></button>
      <button type="button" class="btn btn-light btn-rounded disabled placeholder"></button>
    </div>
  </article>
</template>
