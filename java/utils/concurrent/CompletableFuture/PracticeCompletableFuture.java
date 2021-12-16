package utils.concurrent.CompletableFuture;

import java.time.LocalTime;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.Executors;

class PracticeCompletableFuture {
    public static void main(String[] args) throws Exception {
        CompletableFuture<String> future = new CompletableFuture<>();
        Executors.newCachedThreadPool().submit(() -> {
            Thread.sleep(2000);
            future.complete("Finished");
            return null;
        });
        log(future.get());
    }

    public static void log(String msg) {
        System.out.println(LocalTime.now() + " ("
                + Thread.currentThread().getName() + ") " + msg);
    }
}