<?php
// Dev-only router for `php -S`. Serves files with caching disabled so edits to
// CSS/JS/HTML show up on a normal reload — no hard-refresh while iterating.
// (Headers set before `return false` are dropped for static files, so we serve
// them ourselves here.)

$path = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
$file = realpath(__DIR__ . $path);
$root = realpath(__DIR__);

// Fall back to index.html for the root or any non-file request.
if ($path === '/' || $file === false || !is_file($file)) {
    $file = $root . '/index.html';
}

// Guard against path traversal outside the project root.
if (strpos($file, $root) !== 0) {
    http_response_code(403);
    return true;
}

$types = [
    'html' => 'text/html; charset=utf-8',
    'css'  => 'text/css; charset=utf-8',
    'js'   => 'application/javascript; charset=utf-8',
    'json' => 'application/json; charset=utf-8',
    'svg'  => 'image/svg+xml',
    'png'  => 'image/png',
    'jpg'  => 'image/jpeg',
    'jpeg' => 'image/jpeg',
    'webp' => 'image/webp',
    'gif'  => 'image/gif',
    'ico'  => 'image/x-icon',
    'woff2'=> 'font/woff2',
    'woff' => 'font/woff',
];
$ext = strtolower(pathinfo($file, PATHINFO_EXTENSION));

header('Cache-Control: no-store, no-cache, must-revalidate, max-age=0');
header('Content-Type: ' . ($types[$ext] ?? 'application/octet-stream'));
readfile($file);
return true;
