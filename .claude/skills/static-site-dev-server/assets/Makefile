PORT ?= 8000
HOST ?= localhost

.PHONY: serve
serve: ## start the local dev server (no-cache)
	@echo "Serving on http://$(HOST):$(PORT)"
	php -S $(HOST):$(PORT) -t . dev-router.php

.PHONY: open
open: ## start the server and open a browser
	@( sleep 1 && open "http://$(HOST):$(PORT)" ) &
	@$(MAKE) serve
